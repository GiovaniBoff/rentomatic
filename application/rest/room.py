

import json
import os
from flask import Blueprint, Response, request

from application.rest.dto.room_dto_objects import RoomDTO, create_room_domain_object

from rentomatic.repository.postgres.postgresrepo import PostgresRepo
from rentomatic.requests.room_list import build_room_list_request
from rentomatic.responses import ResponseTypes
from rentomatic.serializers.room import RoomJsonEncoder
from rentomatic.use_cases.room_create import room_create_use_case
from rentomatic.use_cases.room_list import room_list_use_case

blueprint = Blueprint("room", __name__)

STATUS_CODES = {
    ResponseTypes.SUCCESS: 200,
    ResponseTypes.RESOURCE_ERROR: 404,
    ResponseTypes.PARAMETERS_ERROR: 400,
    ResponseTypes.SYSTEM_ERROR: 500,
}

# rooms = [
#     {
#         "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
#         "size": 215,
#         "price": 39,
#         "longitude": -0.09998975,
#         "latitude": 51.75436293,
#     },
#     {
#         "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
#         "size": 405,
#         "price": 66,
#         "longitude": 0.18228006,
#         "latitude": 51.74640997,
#     },
#     {
#         "code": "913694c6-435a-4366-ba0d-da5334a611b2",
#         "size": 56,
#         "price": 60,
#         "longitude": 0.27891577,
#         "latitude": 51.45994069,
#     },
#     {
#         "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
#         "size": 93,
#         "price": 48,
#         "longitude": 0.33894476,
#         "latitude": 51.39916678,
#     },
# ]

postgres_configuration = {
    "POSTGRES_USER": os.environ["POSTGRES_USER"],
    "POSTGRES_PASSWORD": os.environ["POSTGRES_PASSWORD"],
    "POSTGRES_HOSTNAME": os.environ["POSTGRES_HOSTNAME"],
    "POSTGRES_PORT": os.environ["POSTGRES_PORT"],
    "APPLICATION_DB": os.environ["APPLICATION_DB"],
}


@blueprint.route("/rooms", methods=["GET"])
def room_list():

    qrystr_params = {
        "filters": {},
    }

    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_","")] = values

    request_object = build_room_list_request(
        filters=qrystr_params["filters"]
    )

    # repo = MemRepo(rooms)
    repo = PostgresRepo(postgres_configuration)

    response = room_list_use_case(repo, request_object)

    return Response(
        json.dumps(response.value, cls=RoomJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODES[response.type]
    )


@blueprint.route("/rooms", methods=["POST"])
def room_create():
    request_object = request.get_json()

    repo = PostgresRepo(postgres_configuration)

    room_dto = RoomDTO(**request_object)
    room = create_room_domain_object(room_dto)

    response = room_create_use_case(repo, room)

    return Response(
        json.dumps(response.value, cls=RoomJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODES[response.type]
    )
