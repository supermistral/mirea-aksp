import socket, threading, time

from typing import Tuple


HOST = 'localhost'
PORT = 50000
TIMEOUT = 5


class Server:
    def __init__(self, host: str, port: int, timeout: float):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.socket.bind((host, port))
        except socket.error as e:
            print(e)

        self.timeout = timeout
        self.running = True
        self.clients_connections = []
        self.messages = []
        self.lock = threading.Lock()

    def send_bytes(self, conn: socket.socket, msg: bytes) -> None:
        for client_conn in self.clients_connections:
            if client_conn != conn:
                client_conn.send(msg)

    def send_messages(self) -> None:
        while self.running:
            self.lock.acquire()

            for conn, msg in self.messages:
                self.send_bytes(conn, msg)
                time.sleep(0.01)    # prevent message merging

            self.messages = []
            self.lock.release()

            time.sleep(self.timeout)

    def handle_connection(self, conn: socket.socket, addr: Tuple[str, int]) -> None:
        while True:
            data = conn.recv(1024)

            if not data:        # client disconnected
                break

            self.lock.acquire()
            self.messages.append((conn, data))
            self.lock.release()

        self.close_client_connection(conn, addr)

    def run(self) -> None:
        print("Server started")

        self.socket.settimeout(self.timeout)
        self.socket.listen(5)
        first_start = True

        threading.Thread(target=self.send_messages).start()

        while True:
            try:
                conn, addr = self.socket.accept()
            except socket.timeout as e:
                # Finish listening if there are no connections
                if not first_start and len(self.clients_connections) == 0:
                    break
                continue

            print("Connected:", addr)
            self.clients_connections.append(conn)

            threading.Thread(target=self.handle_connection, args=(conn, addr)).start()

            if first_start:
                first_start = False

        self.close()

    def close_client_connection(self, conn: socket.socket, addr: Tuple[str, int]) -> None:
        print('Disconnected:', addr)

        conn.close()
        if conn in self.clients_connections:
            self.clients_connections.remove(conn)

    def close(self) -> None:
        print("Server shutting down...")
        
        for conn in self.clients_connections:
            conn.close()
        self.socket.close()

        self.clients_connections = []
        self.running = False


if __name__ == '__main__':
    server = Server(HOST, PORT, TIMEOUT)
    server.run()
