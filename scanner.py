import socket


def scan(host, port):
    s = socket.socket()
    s.settimeout(1)  # espera maximo 1 segundo por puerto
    try:
        s.connect((host, port))
        print(f"[+] port {port} is open")
    except:
        pass
    finally:
        s.close()


if __name__ == "__main__":
    host = input("host/IP: ")
    start = int(input("start port: "))
    end = int(input("end port: "))

    for port in range(start, end + 1):
        scan(host, port)
