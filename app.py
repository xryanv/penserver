import json
from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "machine_data.json"

# Function to load data from the JSON file
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file doesn't exist or is corrupted

# Function to save data to the JSON file
def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(machine_info_list, file, indent=4)

# Load existing data on startup
machine_info_list = load_data()

# Endpoint to handle incoming data from the client
@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        # Get the JSON data sent from the client
        data = request.get_json()

        # Add a timestamp to the data
        data['timestamp'] = datetime.now().isoformat()

        # Append the received data to the list
        machine_info_list.append(data)

        # Save to JSON file
        save_data()

        # Log the received data
        print("Received data:", data)

        # Return a success response
        return jsonify({"message": "Data received successfully!"}), 201

    except Exception as e:
        print("Error processing request:", e)
        return jsonify({"error": "Failed to process the request."}), 400

# Endpoint to render the HTML page with machine info
@app.route('/')
def index():
    return render_template('index.html', machine_info=machine_info_list)

if __name__ == "__main__":
    # Run the Flask app on the specified host and port
    app.run(host='127.0.0.1', port=5000)
