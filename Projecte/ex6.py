import http.server
import socketserver
import time

def pex6():
    #defineix el port en el que s'executarà
    PORT = 9000

    #configura l'administrador de solicitut HTTP
    request = http.server.SimpleHTTPRequestHandler

    #crear objecte de servidor
    httpd = socketserver.TCPServer(("", PORT), request)

    print(f"El servidor està funcionant en el port {PORT}")

    #temps que durarà el servidor obert(2 min)
    temps = 2*60

    #iniciar el servidor i esperar 2 min
    try:
        httpd.serve_forever()
        time.sleep(temps)
    except KeyboardInterrupt:
        pass

    #després de 2 min tancar
    http.shutdown()
    print(f"El servidor ara està aturat")

