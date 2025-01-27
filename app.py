from flask import Flask, request, jsonify
from pit_token_logic import mint_token, transfer_token, validate_token_logic
from solana_service import create_solana_wallet
from models import db, Agent, PITToken

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pit_agents.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/api/agents/create', methods=['POST'])
def create_agent_route():
    data = request.get_json()
    agent_id = data['agent_id']
    agent = create_solana_wallet(agent_id)
    return jsonify({'message': f'Agent {agent_id} created successfully'}), 201

@app.route('/api/tokens/mint', methods=['POST'])
def mint_token_route():
    data = request.get_json()
    agent_id = data['agent_id']
    token_data = data['token_data']
    
    token = mint_token(agent_id, token_data)  # Logic to mint token
    return jsonify({'message': 'Token minted successfully', 'token': token}), 200

@app.route('/api/tokens/transfer', methods=['POST'])
def transfer_token_route():
    data = request.get_json()
    from_agent_id = data['from_agent_id']
    to_agent_id = data['to_agent_id']
    amount = data['amount']
    
    transfer = transfer_token(from_agent_id, to_agent_id, amount)  # Logic to transfer token
    return jsonify({'message': 'Token transferred successfully', 'transfer': transfer}), 200

@app.route('/api/tokens/validate', methods=['POST'])
def validate_token_route():
    data = request.get_json()
    token_id = data['token_id']
    
    is_valid = validate_token_logic(token_id)  # Validate token conditions
    return jsonify({'is_valid': is_valid}), 200

if __name__ == '__main__':
    app.run(debug=True)
