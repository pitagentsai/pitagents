from flask import Blueprint, request, jsonify
from services.agent_service import AgentService

agent_bp = Blueprint('agent_bp', __name__)

@agent_bp.route('/create', methods=['POST'])
def create_agent():
    data = request.get_json()
    agent_id = data.get('agent_id')

    if not agent_id:
        return jsonify({"message": "agent_id is required."}), 400

    response, status = AgentService.create_agent(agent_id)
    return jsonify(response), status

@agent_bp.route('/', methods=['GET'])
def get_all_agents():
    response, status = AgentService.get_all_agents()
    return jsonify(response), status

@agent_bp.route('/<string:agent_id>/tokens', methods=['GET'])
def get_agent_tokens(agent_id):
    response, status = AgentService.get_agent_tokens(agent_id)
    return jsonify(response), status
