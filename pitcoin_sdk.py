from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# In-memory storage for agents and blockchain (for demo purposes)
agents = {}
blockchain = []


# Simple function to simulate blockchain validation
def validate_blockchain():
    for i in range(1, len(blockchain)):
        if blockchain[i]['previous_hash'] != blockchain[i-1]['hash']:
            return False
    return True

# Endpoint to create an agent
@app.route('/create_agent', methods=['POST'])
def create_agent():
    data = request.get_json()
    agent_id = data.get('agent_id')
    
    if agent_id in agents:
        return jsonify({"message": f"Agent {agent_id} already exists."}), 400
    
    agents[agent_id] = {'tokens': []}
    return jsonify({"message": f"Agent {agent_id} created successfully."})

# Endpoint to add a token to an agent
@app.route('/add_token', methods=['POST'])
def add_token():
    data = request.get_json()
    agent_id = data.get('agent_id')
    token_data = data.get('token_data')
    
    if agent_id not in agents:
        return jsonify({"message": f"Agent {agent_id} does not exist."}), 404
    
    # Generate the block and add it to the blockchain
    new_block = {
        'agent_id': agent_id,
        'token_data': token_data,
        'previous_hash': blockchain[-1]['hash'] if blockchain else None,
    }
    new_block['hash'] = hashlib.sha256(str(new_block).encode('utf-8')).hexdigest()
    blockchain.append(new_block)
    
    agents[agent_id]['tokens'].append(token_data)
    
    return jsonify({"message": "Token added successfully.", "block": new_block})

# Endpoint to get all tokens for an agent
@app.route('/get_tokens/<agent_id>', methods=['GET'])
def get_tokens(agent_id):
    if agent_id not in agents:
        return jsonify({"message": f"Agent {agent_id} does not exist."}), 404
    return jsonify(agents[agent_id]['tokens'])

# Endpoint to validate the blockchain
@app.route('/validate', methods=['GET'])
def validate():
    is_valid = validate_blockchain()
    return jsonify({"is_valid": is_valid})

if __name__ == '__main__':
    app.run(debug=True)
