import os
from azure.ai.openai import OpenAIClient
from azure.core.credentials import AzureKeyCredential

# 設定環境變數 (在命令列或 .env 檔設)
# os.environ['AZURE_OPENAI_API_KEY'] = 'your-api-key'
# os.environ['AZURE_OPENAI_ENDPOINT'] = 'https://your-endpoint.openai.azure.com/'
# os.environ['AZURE_OPENAI_DEPLOYMENT'] = 'gpt-35-turbo'  # 你的部署名

# 取得憑證
api_key = os.getenv('AZURE_OPENAI_API_KEY')
endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
deployment = os.getenv('AZURE_OPENAI_DEPLOYMENT')

if not all([api_key, endpoint, deployment]):
    raise ValueError("請設定 Azure OpenAI 環境變數。")

# 創建客戶端
client = OpenAIClient(endpoint, AzureKeyCredential(api_key))

def get_chat_response(prompt):
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# 簡單命令列互動
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
