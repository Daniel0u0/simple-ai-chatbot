import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load .env file
load_dotenv()

# Read key and endpoint
api_key = os.getenv('AZURE_OPENAI_API_KEY')
endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
deployment = os.getenv('AZURE_OPENAI_DEPLOYMENT')

if not all([api_key, endpoint, deployment]):
    raise ValueError("請設定 .env 檔中的 Azure OpenAI 變數。")

# Create Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-10-21"  # use the latest API version
)

def get_chat_response(prompt):
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Simple command-line interface
print("歡迎使用簡單 Chatbot！輸入 'exit' 結束。")
while True:
    user_input = input("你：")
    if user_input.lower() == 'exit':
        break
    try:
        reply = get_chat_response(user_input)
        print(f"Chatbot：{reply}")
    except Exception as e:
        print(f"錯誤：{e}")