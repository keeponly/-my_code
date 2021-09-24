from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/login")
def login():
    res = dict(request.args)
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)

