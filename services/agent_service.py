from models.agent import Agent
from extensions import db

class AgentService:
    @staticmethod
    def create_agent(agent_id):
        if Agent.query.filter_by(agent_id=agent_id).first():
            return {"message": f"Agent {agent_id} already exists."}, 400

        new_agent = Agent(agent_id=agent_id)
        db.session.add(new_agent)
        db.session.commit()
        return {"message": f"Agent {agent_id} created successfully."}, 201

    @staticmethod
    def get_agent_tokens(agent_id):
        agent = Agent.query.filter_by(agent_id=agent_id).first()
        if not agent:
            return {"message": f"Agent {agent_id} does not exist."}, 404
        return {"tokens": [token.token_data for token in agent.tokens]}, 200

    @staticmethod
    def get_all_agents():
        agents = Agent.query.all()
        return {"agents": [agent.to_dict() for agent in agents]}, 200
