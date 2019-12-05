from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

import psycopg2 as db
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)


conn = db.connect(user='tiling_networks_user', password='password', dbname='tiling_networks', host='127.0.0.1', port='5432')
cursor = conn.cursor(cursor_factory=RealDictCursor)

@app.route('/')
def index():
    return "Hello World"

@app.route('/members')
def members():
    query = 'SELECT * FROM members'

    if request.args.get('community'):
        query += ' WHERE community = %(community)s;'
        cursor.execute(query, { 'community': request.args.get('community') })
    else:
        query += ';'
        cursor.execute(query)

    data = cursor.fetchall()
    return jsonify(data)

@app.route('/communities')
def communities():
    query = 'SELECT * FROM communities'

    if request.args.get('parent'):
        query += ' WHERE parent = %(parent)s;'
        cursor.execute(query, { 'parent': request.args.get('parent') })
    else:
        query += ';'
        cursor.execute(query)

    data = cursor.fetchall()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    