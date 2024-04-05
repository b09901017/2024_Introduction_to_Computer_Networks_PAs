import socket
import sys

# Server setup
# Specify the IP address and port number (Use "127.0.0.1" for localhost on local machine)
# TODO Start
HOST, PORT = "127.0.0.1", 2040
# TODO end


# 1. Create a socket
# 2. Bind the socket to the address
# TODO Start
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
# TODO End

# Listen for incoming connections (maximum of 1 connection in the queue)
# TODO Start
serverSocket.listen(1)
# TODO End

# Start an infinite loop to handle incoming client requests
while True:
    print('Ready to serve...')

    # Accept an incoming connection and get the client's address
    # TODO Start
    connectionSocket, address = serverSocket.accept()
    # TODO End
    print(str(address) + " connected")

    try:
        # Receive and decode the client's request
        # TODO Start
        message = connectionSocket.recv(1024).decode()
        # TODO End

        # If the message is empty, set it to a default value
        if message == "":
            message = "/ /"

        # Print the client's request message
        print(f"client's request message: \n {message}")

        # Extract the filename from the client's request
        # TODO Start
        filename = message.split()[1]
        if filename == "/":
            filename = "index.html"  # Default to index.html if no file specified
        else:
            filename = filename[1:]  # Remove the leading '/'
        # TODO End
        print(f"Extract the filename: {filename}")

        # Open the requested file
        # Read the file's content and store it in a list of lines
        f = open(filename, 'r')
        outputdata = f.read()
        f.close()
        # try:
        #     f = open("index.html", "r")
        #     outputdata = f.readlines()
        #     outputdata_str = ''.join(outputdata)  
        #     print("haha " + outputdata_str)
        # except FileNotFoundError:
        #     print("no file")
        # except Exception as e:
        #     print(f"error : {e}")
        

        # 1. Send an HTTP response header to the client
        # 2. Send the content of the requested file to the client line by line
        # 3. Close the connection to the client
        # TODO Start
        header = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\n\n'
        connectionSocket.send(header.encode("utf-8"))
        connectionSocket.send(outputdata.encode("utf-8"))
        connectionSocket.close()
        # TODO End

    except IOError:
        # If the requested file is not found, send a 404 Not Found response
        # TODO Start
        response = "HTTP/1.1 404 Not Found\n\n404 Not Found"
        connectionSocket.send(response.encode())
        connectionSocket.close()
        # TODO End
