import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10_db_il0a_user:93JffJXJ94OrzLPAK7v5CvAp1GsGS7Si@dpg-cl2iaubmgg9c73aul1l0-a/lab10_db_il0a")
    conn.close()
    return "Database Connection Successful"

