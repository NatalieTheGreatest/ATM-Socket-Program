#MADE BY
#Natalie Friede
#010892127
#I did copy some of this from the tutorials online, but 90% of it is me
    #please no academic integrity I didn't copy from any students
import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 1030  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    choice = 0
    while choice != 4:
        print("Hello! What would you like to do at the bank today? \n")
        print("1)Deposit money\n2)Withdraw money\n3)Check balance\n4)Leave\n****************\n")
        choice = input(" -> ")  # take input
        try:
            int(choice)
        except:
            print("Sorry! That wasn't a valid input. Try entering a number between 1 and 4")
        else:
            #I don't trust doing things in try statements, but this technically could be there instead
            choice = int(choice)
            if(choice > 0 and choice < 5):
                if(choice == 1 or choice == 2):
                    if(choice == 1):
                        print("How much money would you like to deposit? Please enter an integer\n")
                    elif(choice ==2):
                        print("How much money would you like to withdraw? Please enter an integer less than your balance\n")
                    deposit = input(" -> ")
                    try:
                         int(deposit)
                    except:
                        print("That's not an integer")
                    else:
                         deposit = int(deposit)
                         if(deposit < 0):
                             print("You cannot deal with negative numbers\n")
                         else:
                             if(choice == 2):
                                #I know what I said about negative numbers, 
                                #but this makes it so I don't have to have multiple functions for withdraw and deposit
                                deposit*=-1
                             client_socket.send(str(deposit).encode())  # send message
                             data = client_socket.recv(1024).decode()  # receive response
                             print(data)
                elif(choice == 3):
                     #cheeky way of only needing one server side function
                     balanceMessage = '0'
                     client_socket.send(balanceMessage.encode())  # send message
                     data = client_socket.recv(1024).decode()  # receive response
                     print(data)
            else:
                print("That is too large of a number, please try again\n")


        
    client_socket.close()  # close the connection

#I don't know what this is but all the tutorials had it
if __name__ == '__main__':
    client_program()