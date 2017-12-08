
from flask import Flask,request,Response
import json
from sql import sql

app = Flask(__name__)

sql=sql()


@app.route('/')
def blank():
    return json.dumps({})

@app.route('/get_jobs')
def job_list():
    limit = request.args.get('limit', '')
    if limit=='':
        limit='20'
    limit=int(limit)

    results=sql.query()
    if limit==0:
        return json.dumps({})
    if limit>len(results):
        return json.dumps(results)

    else:

        return json.dumps(results[:limit])

if __name__ == '__main__':
    app.run(debug=True)

