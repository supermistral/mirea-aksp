import socket, threading, datetime

from server import HOST, PORT


DISCONNECT_COMMAND = '/q'


class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host: str, port: int) -> None:
        # Setting name
        self.name = input('Enter your name > ').strip()

        try:
            self.socket.connect((host, port))
        except socket.error as e:
            print(e)

    def format_msg(self, msg: str) -> str:
        now = datetime.datetime.now().strftime('%H:%M:%S')
        return f"[{now}] {self.name}: {msg}"

    def handle_msg(self) -> None:
        while True:
            data = self.socket.recv(1024)

            if not data:        # connection rejected by server
                break

            print(data.decode('utf-8'))

        self.socket.close()

    def run(self) -> None:
        threading.Thread(target=self.handle_msg).start()

        while True:
            try:
                client_text = input()
            except (KeyboardInterrupt, EOFError):
                break

            if client_text == DISCONNECT_COMMAND:
                break

            if client_text.strip():
                self.socket.send(str.encode(self.format_msg(client_text)))

        print("Disconnecting...")
        self.socket.shutdown(socket.SHUT_RDWR)


if __name__ == '__main__':
    client = Client()
    client.connect(HOST, PORT)
    client.run()
