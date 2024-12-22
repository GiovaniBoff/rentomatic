
import json
import uuid

import pytest

from rentomatic.domain.room import Room
from rentomatic.serializers.room import RoomJsonEncoder


def test_serialize_domain_room():
    code = uuid.uuid4()

    room = Room(
        code=code,
        size=200,
        price=10,
        longitude=-0.09998975,
        latitude=51.75436293,
    )

    expected_json = f"""
        {{
            "code": "{code}",
            "size": 200,
            "price": 10,
            "longitude": -0.09998975,
            "latitude": 51.75436293
        }}
    """

    json_room = json.dumps(room,cls=RoomJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)


def test_serialize_object_with_missing_attributes():
    class RoomWithMissingAttributes:
        def __init__(self, code):
            self.code = code
    room_with_missing_attributes = RoomWithMissingAttributes("R123")
    with pytest.raises(TypeError):
        json.dumps(room_with_missing_attributes, cls=RoomJsonEncoder)

