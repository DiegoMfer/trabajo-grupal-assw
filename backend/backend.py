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

# Crear tabla y datos de ejemplo
def create_table_and_insert_data():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Crear la tabla si no existe
        cur.execute('''
            CREATE TABLE IF NOT EXISTS alumnos_notas (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL UNIQUE,  -- Agregar UNIQUE para evitar duplicados
                nota INT NOT NULL
            );
        ''')

        # Insertar datos de ejemplo
        cur.execute('''
            INSERT INTO alumnos_notas (nombre, nota)
            VALUES
            ('Juan', 85),
            ('María', 92),
            ('Pedro', 78),
            ('Ana', 90),
            ('Luis', 88)
            ON CONFLICT (nombre) DO NOTHING;  -- Evitar duplicados basados en nombre
        ''')

        # Confirmar la transacción
        conn.commit()
        print("Tabla 'alumnos_notas' creada y datos insertados con éxito.")

    except Exception as e:
        print(f"Error al crear la tabla o insertar datos: {e}")

    finally:
        # Cerrar la conexión a la base de datos
        if conn:
            cur.close()
            conn.close()

# Clase que maneja las peticiones HTTP
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            try:
                conn = get_db_connection()
                cur = conn.cursor()

                # Verificar si la base de datos está funcionando
                cur.execute('SELECT 1')
                result = cur.fetchone()
                conn.close()

                # Crear la respuesta en formato JSON
                response = {
                    "message": f"Hello from Back-end! DB response aa: {result[0]}"
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

        elif self.path == '/alumnos':
            try:
                conn = get_db_connection()
                cur = conn.cursor()

                # Obtener la lista de alumnos y sus notas
                cur.execute('SELECT nombre, nota FROM alumnos_notas')
                alumnos = cur.fetchall()
                conn.close()

                if not alumnos:
                    # Si no hay alumnos, devolver un mensaje adecuado
                    response = {"message": "No se encontraron alumnos en la base de datos."}
                else:
                    # Crear una lista de diccionarios con los alumnos y sus notas
                    alumnos_list = [{"nombre": alumno[0], "nota": alumno[1]} for alumno in alumnos]

                    # Crear la respuesta en formato JSON
                    response = {
                        "alumnos": alumnos_list
                    }

                # Enviar la respuesta con el código 200 OK
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())

            except Exception as e:
                # Capturar cualquier error en la consulta o en la conexión
                print(f"Error al obtener la lista de alumnos: {e}")
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
    create_table_and_insert_data()
    run()
