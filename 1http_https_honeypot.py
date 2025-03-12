



import http.server
import socketserver
import ssl
import threading
import datetime

# Configuration
HTTP_PORT = 8080
HTTPS_PORT = 8443
CERT_FILE = "/home/kali/certs/server.pem"
KEY_FILE = "/home/kali/certs/server.key"

class HoneypotHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        message = f"{timestamp} {self.client_address[0]} {format % args}\n"
        print(message, end='')
        with open("honeypot_log.txt", "a") as log_file:
            log_file.write(message)

def start_http():
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [*] HTTP Honeypot Listening on port {HTTP_PORT}")
    with socketserver.TCPServer(("", HTTP_PORT), HoneypotHTTPRequestHandler) as httpd:
        httpd.serve_forever()

def start_https():
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [*] HTTPS Honeypot Listening on port {HTTPS_PORT}")
    with socketserver.TCPServer(("", HTTPS_PORT), HoneypotHTTPRequestHandler) as httpd:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        httpd.serve_forever()

if __name__ == "__main__":
    try:
        with open(CERT_FILE) as cert_check, open(KEY_FILE) as key_check:
            print("Certificate and key found!")
    except FileNotFoundError:
        print("[!] SSL certificate or key file missing! Check certs/server.pem and certs/server.key.")
        exit(1)

    http_thread = threading.Thread(target=start_http, daemon=True)
    https_thread = threading.Thread(target=start_https, daemon=True)
    
    http_thread.start()
    https_thread.start()
    
    input("Press Enter to stop the honeypot...\n")
