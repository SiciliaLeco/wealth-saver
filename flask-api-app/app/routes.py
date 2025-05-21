from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@api.route('/data', methods=['GET'])
def get_data():
    # Placeholder for data retrieval logic
    return jsonify({"data": "sample data"}), 200

@api.route('/data/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Placeholder for item retrieval logic
    return jsonify({"item_id": item_id, "data": "sample item data"}), 200