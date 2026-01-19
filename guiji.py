# import requests
#
# url = "https://api.siliconflow.cn/v1/messages"
#
# payload = {
#     "model": "deepseek-ai/DeepSeek-V3.2",
#     "messages": [
#         {
#             "role": "user",
#             "content": "你是谁"
#         }
#     ],
#     "max_tokens": 8192
# }
# headers = {
#     "Authorization": "Bearer sk-snpiberuzcieakzbzxhsawcgvqulfbgbjduemndvzqpiqxqh",
#     "Content-Type": "application/json"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(response.text)
from openai import OpenAI
client = OpenAI(
    api_key='sk-snpiberuzcieakzbzxhsawcgvqulfbgbjduemndvzqpiqxqh',
    # 以下是北京地域base_url，如果使用新加坡地域的模型，需要将base_url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
    base_url="https://api.siliconflow.cn/v1",
)
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.2",
    messages=[{'role': 'user', 'content': '你是谁？'}]
)
print(completion)