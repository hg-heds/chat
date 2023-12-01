import socket
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

host = '0.0.0.0'

port = 50001
conexoes = 0
MAX_CLIENT = None
sockets_on = []
sockets_on_lock = Lock()


def client_handler(connection): 
    with connection:
        connection.send(str.encode('Conexão estabelecida... Digite # para finalizar'))
        address = connection.getpeername()
        sockname = f'{address[0]}:{address[1]}'
        print(f'Conectado com: {sockname}')
        while True:
            try:
                data = connection.recv(1024)
            except (Exception, socket.error) as e: 
                print(e)
                break
            except:
                break

            if data == "":
                break
            else:
                message = data.decode('utf-8')
                if message == "#":
                    break
                reply_broadcasting = f'{sockname}: {message}'.encode()
                broadcasting(connection, reply_broadcasting)


    print(f"Conexão finalizada com: {address[0]}:{address[1]}")
    with sockets_on_lock:
        sockets_on.remove(connection)


def broadcasting(sender, message):
    for connection in sockets_on:
        if connection is not sender:
            connection.sendall(message)

def accept_connections(server_socket):
    client, _ = server_socket.accept()
    socket_pool_threads.submit(client_handler, client)
    with sockets_on_lock:
        sockets_on.append(client)

def start_server(host, port):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((host, port))
    except socket.error as e:
        print(str(e))
        return

    print(f'Servidor está ouvindo na porta {port}...')
    server_socket.listen()

    while True:
        accept_connections(server_socket)

if __name__ == '__main__':
    socket_pool_threads = ThreadPoolExecutor(max_workers=MAX_CLIENT)
    start_server(host, port)
    socket_pool_threads.shutdown()