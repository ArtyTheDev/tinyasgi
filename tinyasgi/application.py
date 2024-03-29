import typing

from starlette.middleware.exceptions import ExceptionMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.types import ASGIApp

from tinyasgi.static import DEFAULT_GZIP_PARAMS, \
    DEFAULT_CORS_PARAMS
from tinyasgi.types import ApplicationType
from tinyasgi.wrappers import Request
from tinyasgi.websockets import WebSocket


class Application(object):
    """
        An impl of an ASGI application.
    """
    def __init__(
        self,
        handler: "ApplicationType",
        cors: typing.Dict[
            str, typing.Union[
                tuple, bool
            ]
        ] = DEFAULT_CORS_PARAMS,
        gzip: typing.Optional[bool] = True,
        gzip_params: typing.Dict[str, int] = DEFAULT_GZIP_PARAMS,
        support: typing.Tuple[str] = ("http", "websocket")
    ) -> None:
        self.handler = handler
        self.support = support 

        async def __interal__(scope, recv, send):
            scope_type = scope['type']
            
            if scope_type not in self.support:
                return
            
            if scope_type == "http":
                req = Request(scope, recv, send)
                resp = await handler(req)
                if resp is not None:
                    await resp(scope, recv, send)
            elif scope_type == "websocket":
                req = WebSocket(scope, recv, send)
                await handler(req)

        self.app = ExceptionMiddleware(
            typing.cast(ASGIApp, __interal__)
        )
        self.add_middleware(CORSMiddleware, **cors)

        if gzip is True:
            self.add_middleware(GZipMiddleware, **gzip_params)

    def add_middleware(self, middleware_cls, **params):
        """To append a middleware to the stack."""

        self.app = middleware_cls(self.app, **params)

    async def __call__(self, scope, recv, send):
        await self.app(scope, recv, send) # noqa


def app(
    cors: typing.Dict[
        str, typing.Union[
            tuple, bool
        ]
    ] = DEFAULT_CORS_PARAMS,
    gzip: typing.Optional[bool] = True,
    gzip_params: typing.Dict[str, int] = DEFAULT_GZIP_PARAMS,
    support: typing.Tuple[str] = ("http", "websocket")
):
    """a deco to make an application."""

    def __deco__(func: "ApplicationType"):
        return Application(
            handler=func,
            cors=cors,
            gzip=gzip,
            gzip_params=gzip_params,
            support=support
        )
    return __deco__ # noqa
