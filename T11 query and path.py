#Query Parameters name
#path parameter id

from flask import Flask, request, jsonify

app = Flask(__name__)


data = [
    {"id": 1, "name": "Item One"},
    {"id": 2, "name": "Item Two"}
]


@app.route('/items', methods=['GET'])
def get_items():
    name_query = request.args.get('name')  # Read ?name=... from URL
    if name_query:
        filtered_items = [item for item in data if item['name'].lower() == name_query.lower()]
        return jsonify(filtered_items)
    return jsonify(data)


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404


@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    data.append(new_item)
    return jsonify({"message": "Item added", "item": new_item}), 201

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

