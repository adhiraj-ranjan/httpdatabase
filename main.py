from flask import Flask, jsonify, request, render_template
from api import mngdata as api
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create')
def create():
    key = request.args.get('key')
    value = request.args.get('value')
    
    if not key:
        return jsonify({"response": "invalid arguments"})
    if not value:
        value = ""
    response = api.create(key, value)
        
    if response:
        return jsonify({"key": key,
                        "value": value,
                        "created": "true"})
    else:
        return jsonify({"response": "the key is already present in database",
                        "created": "false"})


@app.route('/get')
def get():
    key = request.args.get('key')
    
    if not key:
        return jsonify({"response": "invalid arguments"})
        
    response = api.get(key)

    if response!=False:
        return jsonify({"key": key,
                        "value": response})
    else:
        return jsonify({"response": "key not found"})

@app.route('/update')
def update():
    key = request.args.get('key')
    value = request.args.get('value')
    if not (key and value):
        return jsonify({"response": "invalid arguments"})

    response = api.update(key, value)

    if response:
        return jsonify({"key": key,
                        "value": value,
                        "updated": "true"})
    else:
        return jsonify({"response": "key not found",
                        "updated": "false"})

@app.route('/delete')
def delete():
    key = request.args.get('key')

    if not key:
        return jsonify({"response": "invalid arguments"})

    if key=="key":
        return jsonify({"response": "this key cannot be deleted",
                        "deleted": "false"})

    response = api.delete(key)

    if response:
        return jsonify({"key": key,
                        "deleted": "true"})
    else:
        return jsonify({"response": "key not found",
                        "deleted": "false"})

if __name__ == '__main__':
    serve(app, host='0.0.0.0')
