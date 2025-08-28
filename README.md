# simple-ai-chatbot

This is a basic Python script that integrates with Azure OpenAI to create a command-line chatbot. It allows users to input messages and receive responses from an AI model.

## Requirements
- Python 3.x
- Packages: `openai`, `python-dotenv` (install via `pip install openai python-dotenv`)

## Setup
1. Create a `.env` file in the project root with the following:
   ```
   AZURE_OPENAI_API_KEY=your-api-key
   AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
   AZURE_OPENAI_DEPLOYMENT=your-deployment-name
   ```
2. Ensure you have an Azure OpenAI deployment set up (e.g., gpt-3.5-turbo model).

## Usage
Run the script:
```
python simple_chatbot.py
```
- Enter your message when prompted.
- Type 'exit' to quit.

Example:
```
你：香港屬於七大洲的哪一個？
Chatbot：香港屬於亞洲大陸。
```

## Notes
- This demo uses Azure OpenAI for responses; real-time data (like weather) may not be accurate.
- For security, API keys are loaded from `.env` and ignored in `.gitignore`.

Thanks for using! If you have issues, check Azure deployment settings.
