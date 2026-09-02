# AI Assistant Chatbot

A smart chatbot built with LangChain that answers different types of questions using advanced AI techniques.

## Features

- **Smart Question Routing**: Automatically detects if your question is about Programming, Math, or General topics
- **Parallel Processing**: Generates answers and summaries at the same time for faster responses
- **Structured Responses**: All answers follow a clear format with confidence level and keywords
- **Chat History**: Keep track of all your conversations in separate chat sessions
- **Easy to Use**: Simple web interface built with Streamlit

## How It Works

### 1. Question Input
You ask a question through the Streamlit chat interface.

### 2. Category Detection
The chatbot analyzes your question and determines its category:
- Programming Questions
- Mathematics Questions
- General Questions

### 3. Smart Processing
The chatbot uses two processes at the same time:
- **Process 1**: Generates the answer for your question using the right expert prompt
- **Process 2**: Creates a summary of your question

### 4. Structured Output
The response is formatted with:
- **Answer**: The complete answer to your question
- **Summary**: A short summary of your question
- **Category**: Programming, Mathematics, or General
- **Confidence**: How confident the AI is (0 to 1)
- **Keywords**: Important words related to the answer

## Project Structure

```
ai_chatbot/
├── app.py              # Streamlit chat interface
├── chatbot.py          # Main chatbot logic with RunnableBranch & RunnableParallel
├── prompts.py          # All prompt templates for different categories
├── schemas.py          # Pydantic schema for structured output
├── requirements.txt    # Python packages needed
├── .env.example        # Example of environment variables
└── README.md          # This file
```

## Installation

### Step 1: Clone the Project
```bash
git clone <your-github-url>
cd ai_chatbot
```

### Step 2: Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On Mac/Linux
```

### Step 3: Install Required Packages
```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Key
1. Get a free API key from [Groq Console](https://console.groq.com)
2. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```
3. Open `.env` and replace `your_actual_api_key_here` with your real API key

### Step 5: Run the Chatbot
```bash
streamlit run app.py
```

The chatbot will open in your browser at `http://localhost:8501`

## Usage

1. **Ask a Question**: Type your question in the chat input box
2. **View Answer**: The AI responds with the answer
3. **See Details**: Click "Structured Output" to see confidence, keywords, and category
4. **Start New Chat**: Click "New Chat" in the sidebar to start a fresh conversation
5. **View History**: All your previous chats are saved in the sidebar

## Technical Details

### RunnableBranch
Routes your question to the right expert based on its category:
```
Question → Classify Category → Route to Expert → Generate Answer
```

### RunnableParallel
Generates multiple outputs at the same time:
```
Question → Generate Answer AND Summary (Parallel)
```

### Pydantic Structured Output
All responses follow the ChatResponse schema:
- Ensures consistent output format
- Validates all fields (confidence between 0-1, category is valid, etc.)
- Type-safe responses

## Technologies Used

- **LangChain**: For building AI chains and workflows
- **Groq API**: For fast AI model responses
- **Streamlit**: For the web chat interface
- **Pydantic**: For data validation with schemas
- **Python-dotenv**: For secure API key management

## Example Questions

**Programming**: "How do I create a React component?"
**Math**: "What is the solution to x² + 5x + 6 = 0?"
**General**: "Tell me about climate change"

## Important Notes

- Your API key is stored in `.env` file (never upload this)
- The `.env.example` file shows what keys you need
- Never share your `.env` file or API keys
- Chat history is stored only in your browser session

## Troubleshooting

**Problem**: "GROQ_API_KEY not found"
- **Solution**: Make sure you created `.env` file and added your API key

**Problem**: "No module named 'langchain'"
- **Solution**: Run `pip install -r requirements.txt`

**Problem**: Chatbot takes too long to respond
- **Solution**: Check your internet connection and Groq API status

## Author

Created as an AI Chatbot Project

## License

This project is open source and available for educational purposes.

---

**Need Help?** Check that all files (app.py, chatbot.py, prompts.py, schemas.py) are in the same folder as this README.
