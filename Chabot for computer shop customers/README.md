# 🤖 Customer Assistant AI Chatbot

This directory contains the **Rasa-based AI Chatbot** designed to assist customers of RK Computers. It handles natural language understanding (NLU), dialogue management, and integrates with the backend to provide real-time information.

## 🏗️ Technical Architecture
- **NLU (Natural Language Understanding)**: Uses Rasa's pipeline to identify user intents (e.g., `check_price`, `ask_availability`) and extract entities (e.g., `laptop`, `RAM`).
- **Dialogue Management**: Managed via Rasa Stories and Rules to ensure a logical flow of conversation.
- **Custom Actions**: Python-based actions (`actions.py`) that connect the bot to external data sources or perform complex logic.

## 📁 File Structure
- `nlu.yml`: Training data for intent recognition.
- `stories.yml`: Conversation patterns.
- `domain.yml`: Defines the chatbot's universe (intents, entities, slots, responses).
- `config.yml`: Model configuration and pipeline settings.
- `actions.py`: Backend logic for dynamic responses.
- `Computer Store.sql`: Database schema for the shop's inventory.

## 🚀 How to Run

### 1. Prerequisites
- Python 3.8 or higher
- Rasa Open Source (`pip install rasa`)

### 2. Training the Model
Whenever you change the NLU data or domain, you must retrain the model:
```bash
rasa train
```

### 3. Running the Action Server
In a separate terminal, start the custom action server:
```bash
rasa run actions
```

### 4. Interacting with the Bot
You can test the bot in the terminal:
```bash
rasa shell
```
Or run the Rasa server with CORS enabled to connect to a frontend:
```bash
rasa run --enable-api --cors "*"
```

## 🧪 Testing
Check the `test cases/` directory for automated conversation tests. Run them using:
```bash
rasa test
```
