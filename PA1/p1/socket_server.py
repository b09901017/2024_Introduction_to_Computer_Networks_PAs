import socket
from datetime import datetime

# Function to calculate the expression
def calculate_expression(expression):
    # TODO: Implement this function
    pass

# Server setup
# Specify the IP address and port number (Use "127.0.0.1" for localhost on local machine)
# TODO Start
HOST, PORT =
# TODO end

with open('./server_log.txt', 'w') as logFile:
    # 1. Create a socket
    # 2. Bind the socket to the address
    # TODO Start
    serverSocket =
    # TODO End

    while True:
        # Listen to a new request with the socket
        # TODO Start
        # TODO End

        now = datetime.now()
        print("The Server is running..")
        logFile.write(now.strftime("%H:%M:%S ") + "The Server is running..\n")
        logFile.flush()


        # Accept a new request and admit the connection
        # TODO Start
        client, address =
        # TODO End

        client.settimeout(15)
        print(str(address) + " connected")
        now = datetime.now()
        logFile.write(now.strftime("%H:%M:%S ") + "connected " + str(address) + '\n')
        logFile.flush()

        try:
            while True:
                client.send(b"Please input a question for calculation")

                # Recieve the data from the client
                # TODO Start
                question =
                # TODO End

                now = datetime.now()
                logFile.write(now.strftime("%H:%M:%S ") + question + '\n')
                logFile.flush()

                # TODO: Call the calculate_expression function here
                ans = calculate_expression(question)

                # Ask if the client want to terminate the process
                message = f"{ans}\nDo you wish to continue? (Y/N)"


                # Send the answer back to the client
                # TODO Start
                # TODO End

                # Terminate the process or continue
                if ans.lower() != 'y':
                    break
        except ConnectionResetError:
            print("Connection reset by peer")
            logFile.write("Connection reset by peer\n")
            logFile.flush()
        except Exception as e:
            print("An error occurred:", e)
            logFile.write(f"An error occurred: {e}\n")
            logFile.flush()

        client.close()

logFile.close()
