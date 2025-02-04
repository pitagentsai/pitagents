# models/block.py
from extensions import db
from utils.hash_utils import generate_hash
import json

class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.String(80), db.ForeignKey('agent.agent_id'), nullable=False)
    token_data = db.Column(db.String(256), nullable=False)
    previous_hash = db.Column(db.String(64))
    hash = db.Column(db.String(64), unique=True, nullable=False)

    def __init__(self, agent_id, token_data, previous_hash=None):
        self.agent_id = agent_id
        self.token_data = json.dumps(token_data)  # Serialize token_data to JSON string
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.agent_id}{self.token_data}{self.previous_hash}"
        return generate_hash(block_string)

    def to_dict(self):
        return {
            'agent_id': self.agent_id,
            'token_data': json.loads(self.token_data),  # Deserialize token_data from JSON string
            'previous_hash': self.previous_hash,
            'hash': self.hash,
            'id': self.id,
        }