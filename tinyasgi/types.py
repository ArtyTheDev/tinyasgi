import typing

if typing.TYPE_CHECKING:
    from tinyasgi.wrappers import Request, Response
    from tinyasgi.websockets import WebSocket


RequestType = typing.Union["Request", "WebSocket"]
ResponseType = typing.Optional["Response"]
CoroRespType = typing.Coroutine[
    typing.Any, typing.Any, ResponseType
]
ApplicationType = typing.Callable[
    [RequestType], CoroRespType
] # noqa