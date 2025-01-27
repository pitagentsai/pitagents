# 🚀 PIT Agent Framework

![PyPI Version](https://img.shields.io/pypi/v/pitagentsai)
![GitHub stars](https://img.shields.io/github/stars/pitagentsai/pitagents?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/pitagentai?style=social)

Welcome to the **PITAGENT Framework** — a powerful system for creating and managing **Programmable Intelligent Tokens (PITs)** on a blockchain! 🌐

This framework allows developers to build and manage programmable tokens that contain specific logic, allowing for flexible and customizable interactions within decentralized applications (dApps) and ecosystems. PIT tokens can be used in a variety of use cases, from finance to gaming, offering secure and intelligent token management.

## Features ✨
- **Agent Management**: Easily create and manage agents (users) with their associated tokens.
- **Programmable Tokens**: Tokens can carry conditions such as time-locks, amounts, or custom logic that must be met before they can be transferred or used.
- **Blockchain Integration**: Interaction with the blockchain (Solana, Ethereum, etc.) for secure and tamper-proof token storage and transactions.
- **Token Conditions**: Programmable logic that defines how tokens can be transferred or used.
- **RESTful API**: Comprehensive API to create agents, mint tokens, transfer tokens, and validate conditions.

## Technologies Used 🛠️
- **Flask**: Lightweight web framework for Python.
- **SQLAlchemy**: ORM (Object-Relational Mapper) for working with databases.
- **Solana** (or **Ethereum**): Blockchain for token management (Solana in this example).
- **Python 3.8+**: Programming language for backend logic.

## Quick Start 🚀

### Prerequisites 📋
- Python 3.8+ installed.
- Flask and other Python libraries.

### Installation 🛠️
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pitagents.git
   cd pitagents
   ```
   
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```
   The Flask server will start at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage 📚

You can interact with the API using tools like **curl**, **Postman**, or any HTTP client of your choice. Below are examples of the API endpoints:

### API Endpoints 📡

#### 1. **Create an Agent**
- **Endpoint**: `/api/agents/create`
- **Method**: `POST`
- **Body**:
   ```json
   {
     "agent_id": "agent_1"
   }
   ```
- **Response**:
   ```json
   {
     "message": "Agent agent_1 created successfully."
   }
   ```

#### 2. **Mint a Token for an Agent**
- **Endpoint**: `/api/tokens/mint`
- **Method**: `POST`
- **Body**:
   ```json
   {
     "agent_id": "agent_1",
     "token_data": {
       "amount": 100,
       "purpose": "Utility token",
       "condition": "time_lock"
     }
   }
   ```
- **Response**:
   ```json
   {
     "message": "Token minted successfully",
     "token": {
       "token_id": "TKN_1627568937",
       "amount": 100,
       "purpose": "Utility token",
       "condition": "time_lock"
     }
   }
   ```

#### 3. **Transfer a Token**
- **Endpoint**: `/api/tokens/transfer`
- **Method**: `POST`
- **Body**:
   ```json
   {
     "from_agent_id": "agent_1",
     "to_agent_id": "agent_2",
     "amount": 50
   }
   ```
- **Response**:
   ```json
   {
     "message": "Token transferred successfully",
     "transfer": {
       "from": "agent_1",
       "to": "agent_2",
       "amount": 50
     }
   }
   ```

#### 4. **Validate Token Conditions**
- **Endpoint**: `/api/tokens/validate`
- **Method**: `POST`
- **Body**:
   ```json
   {
     "token_id": "TKN_1627568937"
   }
   ```
- **Response**:
   ```json
   {
     "is_valid": true
   }
   ```

## Project Structure 📂

```bash
PIT_Framework/
├── app.py               # Main Flask API to interact with the framework
├── pit_token_logic.py   # Logic for minting, transferring tokens and applying conditions
├── solana_service.py    # Interactions with the Solana blockchain
├── models.py            # SQLAlchemy models for Agents and PIT Tokens
├── requirements.txt     # List of project dependencies
└── README.md            # Project documentation (you're here)
```

## Contributing 🤝
We welcome contributions! Feel free to fork the project, make changes, and submit a pull request. Here's how you can contribute:
1. **Fork the repo**
2. **Create a new branch** for your feature or fix:  
   `git checkout -b feature/YourFeature`
3. **Commit your changes**:  
   `git commit -m 'Add new feature'`
4. **Push your branch**:  
   `git push origin feature/YourFeature`
5. **Create a Pull Request**: Open a PR on GitHub.

## License 📄
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact 📧
- Email: [pitagentsdev@gmail.com](mailto:pitagentsdev@gmail.com)
- Twitter: [@pitagentsai](https://twitter.com/pitagentsai)
- GitHub: [@pitagentsai](https://github.com/pitagentsai)

---

## Acknowledgements 🎉
- Inspired by the need for scalable and programmable token systems.
- Built with love using **Flask**, **Solana**, and **SQLAlchemy**.
- Special thanks to the blockchain community for their constant innovation.

---

Happy coding! ✨
