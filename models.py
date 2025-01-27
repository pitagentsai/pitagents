from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.String(120), unique=True, nullable=False)
    public_key = db.Column(db.String(120), unique=True, nullable=False)
    tokens = db.relationship('PITToken', backref='owner', lazy=True)

class PITToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token_id = db.Column(db.String(120), unique=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    purpose = db.Column(db.String(120), nullable=False)
    condition = db.Column(db.String(120), nullable=True)  # Example: time_lock, condition-based transfer
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)
    timestamp = db.Column(db.Integer, default=int(time.time()))  # Store minting timestamp
