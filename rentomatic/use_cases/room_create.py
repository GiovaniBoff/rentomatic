

from rentomatic.responses import (
    ResponseFailure,
    ResponseSuccess,
    ResponseTypes
)


def room_create_use_case(repo, request):
    if not request:
        return ResponseFailure(ResponseTypes.PARAMETERS_ERROR,
                               "Invalid request")
    try:
        room = repo.create(request)
        return ResponseSuccess(room)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
