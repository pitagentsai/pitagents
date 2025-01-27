# 🚀 PIT Agent Framework

![PyPI Version](https://img.shields.io/pypi/v/pitagentsai)
![GitHub stars](https://img.shields.io/github/stars/pitagentsai/pitagents?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/pitagentai?style=social)

A professional and scalable Flask-based Agent AI Framework leveraging PIT (Programmable Intelligent Tokens) for advanced blockchain-like token management. This framework is engineered to efficiently create and manage intelligent agents, securely handle programmable token transactions, and maintain data integrity through a robust blockchain mechanism.

**With PIT, tokens can carry programmable logic, enabling more flexible and intelligent interactions within the agent ecosystem.**

## 🛠️ Features

- **✨ Agent Management**: Easily create and manage agents.
- **🔑 Token Management**: Add, retrieve, and manage tokens associated with agents.
- **🔗 Blockchain Validation**: Ensure the integrity of token transactions using a simple blockchain mechanism.
- **📦 Extensible Structure**: Organized codebase for easy maintenance and scalability.
- **📊 RESTful API**: Comprehensive API endpoints for seamless integration.
- **📚 SQLAlchemy ORM**: Robust database interactions with SQLite for development.

## 🧩 Technologies Used

- **[Flask](https://flask.palletsprojects.com/)**: Web framework for Python.
- **[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)**: ORM for database interactions.
- **[SQLite](https://www.sqlite.org/index.html)**: Lightweight database for development purposes.
- **[Python 3.8+](https://www.python.org/)**: Programming language.

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pitagentsai/pitagents.git
cd pitagents
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.

## 📚 Usage

Interact with the API using tools like `curl`, [Postman](https://www.postman.com/), or any HTTP client of your choice.

### 🧑‍🤝‍🧑 Agent Endpoints

- **Create Agent**

  ```http
  POST /api/agents/create
  ```

  **Body:**

  ```json
  {
    "agent_id": "agent_1"
  }
  ```

- **Get All Agents**

  ```http
  GET /api/agents/
  ```

- **Get Agent Tokens**

  ```http
  GET /api/agents/<agent_id>/tokens
  ```

### 🔗 Blockchain Endpoints

- **Add Token to Agent**

  ```http
  POST /api/blockchain/add_token
  ```

  **Body:**

  ```json
  {
    "agent_id": "agent_1",
    "token_data": "sample_token_data"
  }
  ```

- **Validate Blockchain**

  ```http
  GET /api/blockchain/validate
  ```

## 📝 API Examples

### 1. **Create an Agent**

```bash
curl -X POST http://127.0.0.1:5000/api/agents/create \
-H "Content-Type: application/json" \
-d '{"agent_id": "agent_1"}'
```

**Response:**

```json
{
  "message": "Agent agent_1 created successfully."
}
```

### 2. **Add a Token**

```bash
curl -X POST http://127.0.0.1:5000/api/blockchain/add_token \
-H "Content-Type: application/json" \
-d '{"agent_id": "agent_1", "token_data": "token123"}'
```

**Response:**

```json
{
  "message": "Token added successfully.",
  "block": {
    "agent_id": "agent_1",
    "token_data": "token123",
    "previous_hash": null,
    "hash": "e3b0c44298fc1c149afbf4c8996fb924..."
  }
}
```

### 3. **Get Tokens for an Agent**

```bash
curl http://127.0.0.1:5000/api/agents/agent_1/tokens
```

**Response:**

```json
{
  "tokens": [
    "token123"
  ]
}
```

### 4. **Validate the Blockchain**

```bash
curl http://127.0.0.1:5000/api/blockchain/validate
```

**Response:**

```json
{
  "is_valid": true
}
```

## 📂 Project Structure

```
agent-framework/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── models/
│   ├── __init__.py
│   ├── agent.py
│   └── block.py
├── services/
│   ├── __init__.py
│   ├── agent_service.py
│   └── blockchain_service.py
├── routes/
│   ├── __init__.py
│   ├── agent_routes.py
│   └── blockchain_routes.py
└── utils/
    ├── __init__.py
    └── hash_utils.py
```

## 🧑‍💻 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 📞 Contact

- **Twitter**: [@pitagentsai](https://x.com/pitagentai)
- **GitHub**: [@pitagentsai](https://github.com/pitagentsai)

## 🎉 Acknowledgements

- Inspired by the need for scalable agent and token management systems.
- Built with love using Flask and SQLAlchemy.

---

✨ *Happy Coding!* ✨
```