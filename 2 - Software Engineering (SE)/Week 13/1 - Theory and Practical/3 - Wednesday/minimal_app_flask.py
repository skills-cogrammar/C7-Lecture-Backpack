from flask import Flask, request, jsonify

app = Flask(__name__)  # Create an instance of the Flask class to start the web application

@app.route('/api/hello', methods=['GET'])  # Define a route for the endpoint '/api/hello' that accepts GET requests
def hello_world():  # Define the hello_world function to handle the GET requests to the '/api/hello' endpoint
    return jsonify(message="Hello, World!")  # Return a JSON response with a greeting message


@app.route('/api/greet', methods=['POST'])  # Define a route for the endpoint '/api/greet' that accepts POST requests
def greet():  # Define the greet function to handle the POST requests to the '/api/greet' endpoint
    data = request.get_json()  # Retrieve the JSON data sent in the request
    name = data.get('name', 'World')  # Get the 'name' value from the JSON data, or use 'World' as a default if not provided
    return jsonify(message=f"Hello, {name}!")  # Return a JSON response with a greeting message

if __name__ == '__main__':  # Check if the script is being run directly (not imported as a module)
    app.run(debug=True)  # Run the Flask application with debugging enabled

