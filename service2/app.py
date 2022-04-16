from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
@cross_origin(supports_credentials=True)
def hello_world():

    return jsonify({"status": 200, "message": "service2-version5"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
