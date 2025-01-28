from flask import Flask
from routes.agent_routes import agent_bp
from routes.blockchain_routes import blockchain_bp
from config import Config
from extensions import db  # Import db from extensions.py

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register Blueprints
    app.register_blueprint(agent_bp, url_prefix='/api/agents')
    app.register_blueprint(blockchain_bp, url_prefix='/api/blockchain')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)