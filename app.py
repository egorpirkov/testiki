from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/', methods=['GET'], strict_slashes=False)
def greet():
    return jsonify({"message": "Hello, DevOps Engineer!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6969)