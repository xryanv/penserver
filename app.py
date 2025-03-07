Python ###Python Flask Server###
2	###Version 3###
3	###By Gh0st###
4	
5	from flask import Flask, request, jsonify, render_template
6	from datetime import datetime
7	
8	app = Flask(__name__)
9	
10	# List to store machine info
11	machine_info_list = []
12	
13	# Endpoint to handle incoming data from the client
14	@app.route('/upload', methods=['POST'])
15	def upload_data():
16	    try:
17	        # Get the JSON data sent from the client
18	        data = request.get_json()
19	        
20	        # Add a timestamp to the data
21	        timestamp = datetime.now().isoformat()
22	        data['timestamp'] = timestamp
23	
24	        # Append the received data to the list
25	        machine_info_list.append(data)
26	
27	        # Log the received data
28	        print("Received data:", data)
29	
30	        # Return a success response
31	        return jsonify({"message": "Data received successfully!"}), 201
32	
33	    except Exception as e:
34	        print("Error processing request:", e)
35	        return jsonify({"error": "Failed to process the request."}), 400
36	
37	# Endpoint to render the HTML page with machine info
38	@app.route('/')
39	def index():
40	    return render_template('index.html', machine_info=machine_info_list)
41	
42	if __name__ == "__main__":
43	    # Run the Flask app on the specified host and port
44	    app.run(host='127.0.0.1', port=8000)