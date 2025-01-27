from app import db
from utils.hash_utils import generate_hash

class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.String(80), db.ForeignKey('agent.agent_id'), nullable=False)
    token_data = db.Column(db.String(256), nullable=False)
    previous_hash = db.Column(db.String(64))
    hash = db.Column(db.String(64), unique=True, nullable=False)

    def __init__(self, agent_id, token_data, previous_hash=None):
        self.agent_id = agent_id
        self.token_data = token_data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.agent_id}{self.token_data}{self.previous_hash}"
        return generate_hash(block_string)

    def to_dict(self):
        return {
            'agent_id': self.agent_id,
            'token_data': self.token_data,
            'previous_hash': self.previous_hash,
            'hash': self.hash
        }
