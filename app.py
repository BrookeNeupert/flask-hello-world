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

@app.route('/db_insert')
def insert_db():
    conn = psycopg2.connect("postgres://lab10_db_il0a_user:93JffJXJ94OrzLPAK7v5CvAp1GsGS7Si@dpg-cl2iaubmgg9c73aul1l0-a/lab10_db_il0a")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Values Successfully added to Database"

@app.route('/db_select')
def select():
    conn = psycopg2.connect("postgres://lab10_db_il0a_user:93JffJXJ94OrzLPAK7v5CvAp1GsGS7Si@dpg-cl2iaubmgg9c73aul1l0-a/lab10_db_il0a")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_str = ""
    response_str+="<table>"
    for player in records:
        response_str+="<tr>"
        for info in player:
            response_str+="<td>{}</td>".format(info)
        response_str+="</tr>"
    response_str+="</table>"
    return response_str

#@app.route('/db_drop')
    

    