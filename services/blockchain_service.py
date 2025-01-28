from models.block import Block
from models.agent import Agent
from extensions import db
from utils.hash_utils import generate_hash

class BlockchainService:
    @staticmethod
    def add_token(agent_id, token_data):
        agent = Agent.query.filter_by(agent_id=agent_id).first()
        if not agent:
            return {"message": f"Agent {agent_id} does not exist."}, 404

        last_block = Block.query.order_by(Block.id.desc()).first()
        previous_hash = last_block.hash if last_block else None

        new_block = Block(agent_id=agent_id, token_data=token_data, previous_hash=previous_hash)
        db.session.add(new_block)
        db.session.commit()
        print(new_block.to_dict())
        return {"message": "Token added successfully.", "block": new_block.to_dict()}, 201

    @staticmethod
    def validate_blockchain():
        blocks = Block.query.order_by(Block.id).all()
        for i in range(1, len(blocks)):
            if blocks[i].previous_hash != blocks[i-1].hash:
                return {"is_valid": False}, 200
        return {"is_valid": True}, 200
