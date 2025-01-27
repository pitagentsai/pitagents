import time
from models import PITToken, Agent

# Define token conditions
def mint_token(agent_id, token_data):
    """Create a programmable token for an agent."""
    # Here, we simulate the logic of token minting, such as setting conditions
    token = PITToken(
        agent_id=agent_id,
        amount=token_data['amount'],
        token_id="TKN_" + str(int(time.time())),
        purpose=token_data['purpose'],
        condition=token_data.get('condition', None)  # Store the condition of the token (e.g., time-lock)
    )
    
    # Logic for minting token into Solana or Ethereum could go here
    # Save token to the database
    db.session.add(token)
    db.session.commit()
    
    return token

def transfer_token(from_agent_id, to_agent_id, amount):
    """Transfer tokens between two agents."""
    from_agent = Agent.query.filter_by(agent_id=from_agent_id).first()
    to_agent = Agent.query.filter_by(agent_id=to_agent_id).first()
    
    # Find token owned by from_agent
    token = PITToken.query.filter_by(agent_id=from_agent_id).first()
    
    if not validate_token_logic(token.token_id):
        return {"message": "Token cannot be transferred due to unmet conditions."}
    
    # Simulate transfer logic (in reality, you would interact with the blockchain here)
    transfer = {
        'from': from_agent.agent_id,
        'to': to_agent.agent_id,
        'amount': amount,
        'status': 'success'
    }
    
    return transfer

def validate_token_logic(token_id):
    """Validate the token logic based on predefined conditions."""
    token = PITToken.query.filter_by(token_id=token_id).first()
    
    if token.condition == 'time_lock':
        current_time = int(time.time())
        # Example: Condition to allow transfer only after 24 hours
        if current_time - token.timestamp < 86400:  # 24 hours in seconds
            return False
    return True
