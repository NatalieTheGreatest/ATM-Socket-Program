#MADE BY
#Natalie Friede
import socket
balance = 100

def server_program():
    global balance
    # get the hostname
    host = socket.gethostname()
    port = 1030  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    #you can only log in 5 times
    server_socket.listen(1)
    conn, addr = server_socket.accept()  # accept new connection
    while True:
        try:
            message = ""
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(2048).decode()
            try: 
                data = int(data)
            except:
                message = "Sorry! Something went wrong\n"
            else:
                tempBalance = balance
                balance += data
                if(balance < 0):
                    message = "You cannot have a negative balance. Withdraw the amount you have or less\n"
                    balance = tempBalance
                else:
                    message = "Your balance is currently " + str(balance)
            conn.send(message.encode())  # send data to the client
        except(Exception):
            print("Client probably left\n")
            server_socket.listen(1)
            conn, addr = server_socket.accept()
           
    conn.close()


if __name__ == '__main__':
    server_program()
