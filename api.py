import pymysql
from flask import Flask, request, Response
import json

server = 'localhost'
database = 'printer'
user = 'root'

# database connection
conn = pymysql.connect(host = server, user = user, db = database)
if (conn):
    print('Connection to MySQL database', database, 'was successful!')
cursor = conn.cursor()
# cursor.execute('DESC job_history;')
# row=cursor.fetchone()
# while row:
#     print(row)
#     row=cursor.fetchone()
app = Flask(__name__)

@app.route('/get_jobs')
def job_list():
    cursor.execute('SELECT * FROM job_history;')
    row=cursor.fetchone()
    results=[]
    while row:
        results.append({'filename': row[1],
                        'details': {'printer': row[0], 'starttime': row[2], 'endtime': row[3], 'status': row[4]}})
        row=cursor.fetchone()
    return json.dumps(results)