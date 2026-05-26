from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def greet():
    return jsonify({"message": "Hello, DevOps Engineer!"})

if __name__ == '__main__':
    app.run(port=6969)