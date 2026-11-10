import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '"Hello World from Layce in 3308"'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://lab10_oyps_user:Gu6iR4E2FTf8OjsY2O34WzLlfsxSk2ah@dpg-dbp4ba142hec73bhoh30-a/lab10_oyps")
    conn.close()
    return "Database Connection Successful"