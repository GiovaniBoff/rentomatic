from unittest import mock
import uuid
import pytest

from rentomatic.domain.room import Room
from rentomatic.responses import ResponseTypes
from rentomatic.use_cases.room_create import room_create_use_case


@pytest.fixture
def domain_rooms():
    room_1 = Room(
        code=uuid.uuid4(),
        size=215,
        price=39,
        longitude=-0.09998975,
        latitude=51.75436293,
    )

    room_2 = Room(
        code=uuid.uuid4(),
        size=405,
        price=66,
        longitude=0.18228006,
        latitude=51.74640997,
    )

    room_3 = Room(
        code=uuid.uuid4(),
        size=56,
        price=60,
        longitude=0.27891577,
        latitude=51.45994069,
    )

    room_4 = Room(
        code=uuid.uuid4(),
        size=93,
        price=48,
        longitude=0.33894476,
        latitude=51.39916678,
    )

    return [room_1, room_2, room_3, room_4]


def test_room_create(domain_rooms):
    repo = mock.Mock()
    repo.create.return_value = domain_rooms[0]

    request = domain_rooms[0]
    response = room_create_use_case(repo, request)

    assert bool(response) is True
    repo.create.assert_called_with(request)
    assert response.value == domain_rooms[0]


def test_room_create_with_empty_request():
    repo = mock.Mock()

    request = None
    response = room_create_use_case(repo, request)

    assert bool(response) is False
    repo.create.assert_not_called()


def test_room_create_handles_generic_error(domain_rooms):
    repo = mock.Mock()
    repo.create.side_effect = Exception("Just an error message")

    request = domain_rooms[0]
    response = room_create_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }
