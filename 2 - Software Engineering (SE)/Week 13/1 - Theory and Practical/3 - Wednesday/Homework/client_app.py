from flask import Flask, request

app = Flask(__name__)

@app.route("/api/v1/", methods=["GET"])
def hello_world():
    return "Hello, world!"

@app.route("/api/v1/", methods=["POST"])
def greet():
    data = request.get_json()
    name = data.get("name", "default")
    return f"Hello, {name}!"""

if __name__ == "__main__":
    app.run(debug=True)