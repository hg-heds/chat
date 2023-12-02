import socket
from ui import APP
from threading import Thread,Lock
host = input("HOST: ") or '127.0.0.1'
port = int (input("PORT: ") or 50001)

iostream_lock = Lock()

def receive(client_socket, print_function, bool_running):
    client_socket.settimeout(1)
    while bool_running():
        try:
            response = client_socket.recv(1024)
            if response:
                print_function(response.decode('utf-8'))
        except socket.timeout:
            pass
        except Exception as e:
            print(e)
            break
        except:
            break


try:
    user_interface = APP()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

        print('Esperando pela conexão...')
        client_socket.connect((host, port))
        response = client_socket.recv(1024)
        if response:
            print(response.decode('utf-8'))
        receive_thread = Thread(target=receive, args=(client_socket,user_interface.ins,user_interface.running))
        receive_thread.start()

        user_interface.send_function = lambda message: client_socket.send(message.encode('utf-8'))
        user_interface.start()


    print("Finalizou conexão...")

except(Exception, socket.error) as e:
    print(str(e))
except:
    print("Erro se detecção")
    