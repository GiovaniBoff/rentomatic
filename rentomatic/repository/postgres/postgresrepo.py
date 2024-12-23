import code
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rentomatic.domain import room
from rentomatic.repository.postgres.postgres_objects import Base, Room


class PostgresRepo:
    def __init__(self, configuration):
        connection_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            configuration["POSTGRES_USER"],
            configuration["POSTGRES_PASSWORD"],
            configuration["POSTGRES_HOSTNAME"],
            configuration["POSTGRES_PORT"],
            configuration["APPLICATION_DB"],
        )

        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine


    def _create_room_objects(self, results):
        return [
            room.Room(
                code=q.code,
                size=q.size,
                price=q.price,
                latitude=q.latitude,
                longitude=q.longitude,
            )
            for q in results
        ]

    def _create_room_object(self, result):
        return room.Room(
            code=result.code,
            size=result.size,
            price=result.price,
            latitude=result.latitude,
            longitude=result.longitude,
        )

    def _create_room_sql_object(self, room):
        return Room(
            code=str(room.code),
            size=room.size,
            price=room.price,
            latitude=room.latitude,
            longitude=room.longitude
        )

    def list(self, filters=None):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        query = session.query(Room)

        if filters is None:
            return self._create_room_objects(query.all())

        if "code__eq" in filters:
            query = query.filter(Room.code == filters["code__eq"])

        if "price__eq" in filters:
            query = query.filter(Room.price == filters["price__eq"])

        if "price__lt" in filters:
            query = query.filter(Room.price < filters["price__lt"])

        if "price__gt" in filters:
            query = query.filter(Room.price > filters["price__gt"])

        return self._create_room_objects(query.all())

    def create(self, room):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        session.add(self._create_room_sql_object(room))
        session.commit()

        return self._create_room_object(room)
