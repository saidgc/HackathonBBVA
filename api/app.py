from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    print(request.args['user'])
    print(request.args['pass'])
    return jsonify(request.json)


if __name__ == "__main__":
    app.run()
