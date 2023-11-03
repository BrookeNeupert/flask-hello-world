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

@app.route('/db_create')
def create_db():
    conn = psycopg2.connect("postgres://lab10_db_il0a_user:93JffJXJ94OrzLPAK7v5CvAp1GsGS7Si@dpg-cl2iaubmgg9c73aul1l0-a/lab10_db_il0a")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Created"

