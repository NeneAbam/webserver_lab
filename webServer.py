from socket import *
import sys

def webServer(serverPort):

    # Create server socket
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare the server socket
    serverSocket.bind(('', serverPort))

    # Fill in start
    serverSocket.listen(1)
    # Fill in end

    print('Ready to serve...')

    while True:

        # Fill in start
        connectionSocket, addr = serverSocket.accept()
        # Fill in end

        try:

            # Fill in start
            message = connectionSocket.recv(1024).decode()
            # Fill in end

            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            # Fill in start
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            # Fill in end

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

        except IOError:

            # Fill in start
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
            connectionSocket.close()
            # Fill in end

    serverSocket.close()

if __name__ == "__main__":
    webServer(13331)
