import socket
from ui import APP
from threading import Thread,Lock
host = input("HOST: ") or '127.0.0.1'
port = int (input("PORT: ") or 50001)

iostream_lock = Lock()

def receive(client_socket, print_function, loop_function):
    client_socket.settimeout(1)
    while loop_function():
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
    ui = APP()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

        print('Esperando pela conexão...')
        client_socket.connect((host, port))
        response = client_socket.recv(1024)
        if response:
            print(response.decode('utf-8'))

        receive_thread = Thread(target=receive, args=(client_socket,ui.ins,ui.running))
        receive_thread.start()


        ui.send_function = lambda x: client_socket.send(x.encode('utf-8'))
        ui.start()


    print("Finalizou conexão...")

except (Exception, socket.error) as e:
    print(str(e))
except:
    print("Erro se detecção")



