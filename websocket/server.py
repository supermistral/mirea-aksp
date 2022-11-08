import asyncio, websockets, signal


HOST = 'localhost'
PORT = 8080


async def main_handler(ws: websockets.WebSocketServerProtocol, uri: str) -> None:
    while True:
        if uri == '/webs':
            data = await ws.recv()
            print(f"Recieved: {data}")

            if data == '/q':
                return

            await ws.send(data)
        else:
            return


async def serve() -> None:
    # Terminate process when it receives SIGTERM signal, i.e. 'kill -SIGTERM <pid>'
    loop = asyncio.get_event_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)
    
    async with websockets.serve(main_handler, HOST, PORT):
        await stop


if __name__ == '__main__':
    asyncio.run(serve())
