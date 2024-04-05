import socket
from datetime import datetime

# Function to calculate the expression
def calculate_expression(expression):
    operands = expression.split()
    if len(operands) == 3:
        num1, operator, num2 = operands
        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            return str(num1 + num2)
        elif operator == '-':
            return str(num1 - num2)
        elif operator == '*':
            return str(num1 * num2)
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero."
            return str(num1 / num2)
        elif operator == '**':
            return str(num1 ** num2)
        elif operator == '%':
            if num2 == 0:
                return "Error: Division by zero."
            return str(num1 % num2)
        elif operator == '//':
            if num2 == 0:
                return "Error: Division by zero."
            return str(num1 // num2)
        else:
            return "Error: Invalid operator."
    elif len(operands) == 2:
        operator, num = operands
        num = float(num)
        
        if operator == 'sqrt':
            return str(num ** 0.5) if num >= 0 else "Error: Negative number cannot be square rooted."
        elif operator == 'abs':
            return str(abs(num))
        else:
            return "Error: Invalid operator or format."
    else:
        return "Error: Invalid expression format."


    

# Server setup
# Specify the IP address and port number (Use "127.0.0.1" for localhost on local machine)
# TODO Start
HOST, PORT = "127.0.0.1", 2040
# TODO end

with open('./server_log.txt', 'w') as logFile:
    # 1. Create a socket
    # 2. Bind the socket to the address
    # TODO Start
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((HOST, PORT))
    # TODO End

    while True:
        # Listen to a new request with the socket
        # TODO Start
        serverSocket.listen()
        # TODO End

        now = datetime.now()
        print("The Server is running..")
        logFile.write(now.strftime("%H:%M:%S ") + "The Server is running..\n")
        logFile.flush()


        # Accept a new request and admit the connection
        # TODO Start
        client, address = serverSocket.accept()
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
                question = client.recv(1024).decode('utf-8')
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
                client.sendall(message.encode('utf-8'))
                # TODO End
                decision = client.recv(1024).decode('utf-8').strip()
                if decision.upper() == 'N':
                    break
                # Terminate the process or continue
                # if ans.lower() != 'y':
                #     break
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
