
from openai import OpenAI
client = OpenAI(
    api_key='bce-v3/ALTAK-zpfMF1OB0JJxHBeeUHvAb/aedb37dbdbd578d9b383ed11166933acdee02348',

    base_url="https://qianfan.baidubce.com/v2",
)
completion = client.chat.completions.create(
    model="ernie-4.5-turbo-128k",
    messages=[{'role': 'user', 'content': '你是谁？'}]
)
print(completion.choices[0].message.content)
