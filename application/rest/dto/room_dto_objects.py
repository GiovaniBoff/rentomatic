import uuid
from pydantic import BaseModel

from rentomatic.domain import room


class RoomDTO(BaseModel):
    size: int
    price: int
    longitude: float
    latitude: float


def create_room_domain_object(room_dto):
    return room.Room(
        code=uuid.uuid4(),
        size=room_dto.size,
        price=room_dto.price,
        longitude=room_dto.longitude,
        latitude=room_dto.latitude
    )
