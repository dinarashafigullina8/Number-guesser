import json
import socket
import sys
import syslog

syslog.openlog(sys.argv[0], syslog.LOG_SYSLOG) 

def start_server():
    try:
        syslog.syslog(syslog.LOG_INFO, "Server in operation")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 2000))
        server.listen(2)
        while True:
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            content = get_request(data)
            syslog.syslog(syslog.LOG_INFO, "Successful connection")
            HDRS ='HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n'
            content2 = json.dumps(content,indent=4).encode('utf-8')
            client_socket.send(HDRS.encode('utf-8') + content2)
            client_socket.shutdown(socket.SHUT_WR)
            syslog.syslog(syslog.LOG_INFO, "Result available")
    except KeyboardInterrupt:
        server.close()
        syslog.syslog(syslog.LOG_ERR, "Server is not available")
      
   
                

def get_request(request_data):
    syslog.syslog(syslog.LOG_INFO, "Proccessing")
    path = request_data.split('/')
    if(path[1] != 'scan'):
        syslog.syslog(syslog.LOG_ERR, "incorrect method, not scan")
        return 'incorrect method, not scan, use /scan/<ip>/<begin_port>/<end_port>'
   
    syslog.syslog(syslog.LOG_INFO, "Correct address")
    ip = path[2]
    begin_port = int(path[3])
    end_port = int(path[4].split(' ')[0])
    if (begin_port<0) or (end_port<0) or (begin_port>65535) or (end_port>65535):
        syslog.syslog(syslog.LOG_ERR, "incorrect port")
        return 'incorrect port, port must be 0-65535'
    scanner = []
    for port in range(begin_port, end_port+1):
        sock = socket.socket()
        sock.settimeout(1)
        try:
            sock.connect((ip, port))
        except socket.error:
            dict = {"port": port, "state": "close"}
        else:
            sock.close 
            dict = {"port":port, "state": "open"}
        scanner.append(dict)
    return scanner
        


if __name__ == '__main__':
    start_server()

syslog.closelog()

