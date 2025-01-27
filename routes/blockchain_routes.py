from flask import Blueprint, request, jsonify
from services.blockchain_service import BlockchainService

blockchain_bp = Blueprint('blockchain_bp', __name__)

@blockchain_bp.route('/add_token', methods=['POST'])
def add_token():
    data = request.get_json()
    agent_id = data.get('agent_id')
    token_data = data.get('token_data')

    if not agent_id or not token_data:
        return jsonify({"message": "agent_id and token_data are required."}), 400

    response, status = BlockchainService.add_token(agent_id, token_data)
    return jsonify(response), status

@blockchain_bp.route('/validate', methods=['GET'])
def validate_blockchain():
    response, status = BlockchainService.validate_blockchain()
    return jsonify(response), status
