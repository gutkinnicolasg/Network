import socket
import sys

# Port Scanner for TCP Ports
# by Guillaume Gutkin-Nicolas

# Disclaimer: Scanning a port is the equivalent of walking up to a door and checking if
# it is locked. If the door doesn't belong to you would it be considered trespassing?
# Something to consider before using this tool

# Ask for input for global variable
host = input("Enter a remote host to scan: ")
# deals with input that's not in IP format
hostIP = socket.gethostbyname(host)

# singlePort function
def singlePort():
    port = int(input("What port would you like to scan: "))
    # print statement to seperate the prompt from result
    print("-" * 60)
    # try to open a socket and get a result
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hostIP, port))
        if result == 0:
            print("Port", port, "   Open")
        else:
            print("Port", port, "   Closed TCP error code", result)
        sock.close()
    # except socket error and exit system
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

# rangePort function
def rangePort():
    start = int(input("What port would you like to start at: "))
    end = int(input("What port would you like to end at: "))
    # print statement to seperate the prompt from result
    print("-" * 60)
    # try to open a socket and get a result
    try:
        # loop through the range given
        for port in range(start,end):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((hostIP, port))
            if result == 0:
                print("Port", port, "   Open")
            else:
                print("Port", port, "   Closed TCP error code", result)
            sock.close()
    # except socket error and exit system
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

# main function
if __name__=="__main__":
    choice = input("Would you like to scan a single port(S) or range or ports(R)?: ")
    if choice == 'S' or choice == 's':
        singlePort()
    elif choice == 'R' or choice == 'r':
        rangePort()
    else:
        print("No ports will be scanned. Goodbye...")
  

