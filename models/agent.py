from app import db

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.String(80), unique=True, nullable=False)
    tokens = db.relationship('Block', backref='agent', lazy=True)

    def to_dict(self):
        return {
            'agent_id': self.agent_id,
            'tokens': [token.token_data for token in self.tokens]
        }
