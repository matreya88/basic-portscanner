import socket


def scan_port(ipaddr, ports):
    print("Start scanning " + ipaddr)
    for port in range(int(ports)):
        try:
            s = socket.socket()
            s.connect((ipaddr, port))
            print(f"Port {port} is open!!! - {ports - int(port)} more ports left to scan.")
            s.close()
        except socket.error:
            print("It was not possible to connect to the selected host")


def choose_targets():
    ipaddr = input("what IP address do you want to scan?")
    ports = input("how many ports you want to scan?")
    scan_port(ipaddr, ports)
    print("Scan completed!")


choose_targets()
