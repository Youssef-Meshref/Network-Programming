import socket , threading 


clients = []

def handle_client(conn , addr ) :
    while True : 
        try : 
            message_bytes_length = conn.recv(8)
            message_length = int.from_bytes(message_bytes_length , "big")
            message = conn.recv(message_length).decode("utf-8")
            
            if not message : 
                break ; 
            print(f"received message from {addr} says : {message.split(':')[0]}")
            
            recipient_address , data =message.split(":" , 1)
            
            recipient_socket = None 
            for recipient_conn , recipient_addr in clients :
                print(recipient_addr , recipient_address , message , sep="**") 
                if str(recipient_addr) == recipient_address : 
                    recipient_socket = recipient_conn 
                
            if recipient_socket : 
                recipient_socket.send(message_bytes_length)
                recipient_socket.send(data.encode("utf-8"))
            else :
                print("Recipient Not Founded")
        except : 
            break
        
    print(f"Connection closed with {addr}")
    clients.remove((conn, addr))
    conn.close()
        
        
hostname=  "localhost" 
port = 8001

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
sock.bind((hostname , port) )
sock.listen(5)



while True :  
    conn , addr = sock.accept() 
    clients.append((conn , addr)) 
    client_thread = threading.Thread(target=handle_client , args=(conn , addr) )
    print(f"Connected with {addr}")
    client_thread.start()
    