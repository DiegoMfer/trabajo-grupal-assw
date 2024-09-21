import json
import psycopg2
from http.server import BaseHTTPRequestHandler, HTTPServer

# Conectar a la base de datos PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host="db-service",
        database="mydb",
        user="postgres",
        password="password"
    )
    return conn

# Clase que maneja las peticiones HTTP
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            try:
                conn = get_db_connection()
                cur = conn.cursor()
                cur.execute('SELECT 1')
                result = cur.fetchone()
                conn.close()

                # Crear la respuesta en formato JSON
                response = {
                    "message": f"Hello from Back-end! DB response: {result[0]}"
                }

                # Enviar la respuesta con el código 200 OK
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())

            except Exception as e:
                # En caso de error, enviar un mensaje de error
                self.send_response(500)
                self.end_headers()
                self.wfile.write(f"Error: {e}".encode())

# Configurar y ejecutar el servidor HTTP
def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
