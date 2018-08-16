from flask import Flask, request, redirect
from flask import jsonify
import json, time

app = Flask(__name__, static_url_path='')

max_store = 10
content = []

@app.route('/easypaste', methods=['GET', 'POST'])
def easypaste():
    t = request.form['easypaste']
    content.insert(0, (t, str(time.time()).replace('.', '')))
    while len(content) > max_store:
        content.pop()
    return jsonify({'result': 'success'})

@app.route('/query', methods=['GET'])
def query():
    return jsonify(content)

@app.route('/', methods=['GET'])
def index():
    return redirect('/index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)