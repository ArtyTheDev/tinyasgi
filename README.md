# TinyASGI
A little ASGI tool-kit to help you build your framework.

- Fully typed with no errors.
- Based on PEP8 and flake8.
- Starlette standard config.
- Asgiref typing.
- Support both HTTP and WebSockets.

## Example
```py
import tinyasgi

@tinyasgi.application()
async def main(request: tinyasgi.RequestType) -> tinyasgi.ResponseType:
    # To check if the connection is a websocket
    # we use the `isinstance` method to check
    # if the class is a `tinyasgi.WebSocket`
    if isinstance(request, tinyasgi.WebSocket):
        # Accept the connection.
        await request.accept()

        while True:
            try:
                # Receive the text.
                recv = await request.receive_text()
                print(recv)
            except tinyasgi.WebSocketDisconnect:
                break
        
    if isinstance(request, tinyasgi.Request):
        return tinyasgi.PlainTextResponse("Hello, World")
```

## Install
- You need git to install it.
```
pip install git+https://github.com/ArtyTheDev/tinyasgi.git
```