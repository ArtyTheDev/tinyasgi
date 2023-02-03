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
        