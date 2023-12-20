import socket as ss
from threading import Thread

class Server:
    def __init__(self):
        self.routes = {
            "/pato": {
                    "data_type": "text",
                    "data": "pato"
                },
            "/batata": {
                    "data_type": "html",
                    "data": "<h1>Batata</h1> </br> <p> opa teste</p>"
                }
        }
        self.socket = self.start_server()
        self.accept_clients()

    def recv_data(self, client: ss.socket) -> str:
        while True:
            package = client.recv(1024)
            if package:
                return package.decode("utf-8")

    def send_data(self, client: ss.socket, data_type: str, data: str):
        if data_type == "html":
            msg = f"HTTP/1.1 200 OK\r\nContent-Type text/html\r\n\r\n{data}"
        elif data_type == "text":
            msg = f"HTTP/1.1 200 OK\r\n\r\n{data}"

        client.send(msg.encode("utf-8"))

    def handle_client(self, client: ss.socket, adress: tuple[str, int]):
        print(f"Client {adress[0]} conectado!")
        request = self.recv_data(client)
        route = self.handle_request(request)

        print([route, ])

        if route in self.routes.keys():
            data_type = self.routes[route]["data_type"]
            data = self.routes[route]["data"]
            self.send_data(client, data_type, data)
        else:
            self.send_data(client, "text", "Route not found!")
        client.close()

    def handle_request(self, request: str) -> str:
        final_route = request.index(" HTTP/1.1")
        return request[4:final_route]

    def accept_clients(self):
        while True:
            client, adress = self.socket.accept()
            Thread(target=self.handle_client, args=[client, adress]).start()

    def start_server(self):
        socket = ss.socket(ss.AF_INET, ss.SOCK_STREAM)
        ip_adress = ss.gethostbyname(ss.gethostname())
        socket.bind((ip_adress, 20000))
        socket.listen(5)
        print("server started")
        print(ip_adress)

        return socket

Server = Server()