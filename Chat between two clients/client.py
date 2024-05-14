import threading , socket 


hostname = "localhost"
port = 8001


def receive_message(sock) : 
    while True : 
        try : 
            message_bytes_length = sock.recv(8)
            message_length = int.from_bytes(message_bytes_length , "big")
            data = sock.recv(message_length).decode("utf-8")
            print(data)
        except sock.error :
            print("Connection error while receiving message from server :(")
        except : 
            print("Error happen while receiving message from server :(")

def send_message(sock) : 
    while True : 
        try : 
            data = input("")
            recipient = input("enter the recipient address (host:port)")
            message = f"{recipient}:{data}"
            
            message_size = len(message) 
            sock.send(message_size.to_bytes(8 , "big"))
            sock.send(message.encode("utf-8")) 
        except sock.error : 
            print("Connection Error while sending your message :(")
        except : 
            print("Error Happen while sending your message :(")
             
            
sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 

sock.connect((hostname , port))



receive_thread = threading.Thread(target=receive_message , args=(sock ,))
receive_thread.start()


send_thread = threading.Thread(target=send_message , args=(sock ,))
send_thread.start()