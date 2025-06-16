from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"}
]

# GET method
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# POST method
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    data.append(new_item)
    return jsonify({"message": "Item added", "item": new_item}), 201

if __name__ == '__main__':
    app.run(debug=True)
