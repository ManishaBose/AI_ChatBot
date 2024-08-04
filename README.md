# AI Chatbot with Ollama and LangChain

This project is an AI chatbot that uses Ollama's local language models and LangChain for easy interaction. It maintains conversation context and provides responses based on the input and conversation history.

## Prerequisites

- Python 3.7+
- Ollama installed on your system (https://ollama.com/download)
- LangChain library

## Setup

1. Clone this repository:

   ```
   git clone https://github.com/ManishaBose/AI_ChatBot.git
   ```

   ```
   cd AI_ChatBot
   ```

2. Create a virtual environment:

   ```
   python3 -m venv chatbot
   ```

3. Activate the virtual environment:
   - On macOS and Linux:
   ```
   source chatbot/bin/activate
   ```
   - On Windows:
   ```
   chatbot\Scripts\activate
   ```
4. Install the required packages:

   ```
   pip install langchain langchain-ollama ollama
   ```

5. Ensure Ollama is running on your system with the "llama3.1" model. If you haven't downloaded it yet, run:
   ```
   ollama pull llama3.1
   ```

## Usage

1. Run the chatbot:

   ```
   python3 main.py
   ```

2. Start chatting with the AI. Type your messages and press Enter.

3. To exit the conversation, type 'exit' and press Enter.
