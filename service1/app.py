from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello_world():

    return jsonify({"status": 200, "message": "service1-version1"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
