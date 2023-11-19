import socket

def port_scan(target, start_port, end_port):
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

target = input("Hedef IP adresini girin: ")
start_port = int(input("Tarama başlangıç portunu girin: "))
end_port = int(input("Tarama bitiş portunu girin: "))

port_scan(target, start_port, end_port)