from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Conectar a la base de datos PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(host="db-service", database="mydb", user="postgres", password="password")
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT 1')
    result = cur.fetchone()
    conn.close()
    return jsonify({"message": f"Hello from Back-end! DB response: {result[0]}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
