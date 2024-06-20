from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return {"message": "Hello world"}

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")