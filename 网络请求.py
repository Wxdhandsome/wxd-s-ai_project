
import requests

# # respond=requests.get('https://httpbin.org/get')
# # print(respond.text)
# # print(respond.status_code)
# data_2=['我是王晓端']
# # data={'uesrname':{'admin'},'password':'123456'}
# respond_2=requests.post('https://httpbin.org/post',json=data_2)
# print(respond_2.status_code)
# print(respond_2.text)
#


# apiKey='9f8f1aabf8381e5592d600d9c92956e7'
# url='https://apis.juhe.cn/iplocation/ipv4dist/query'
# params={
#     'key':apiKey,
#     'ip':'119.29.29.29'
# }
# response =requests.get(url=url,params=params)
# if response.status_code==200:
#     print(response.json())
# else:
#     print('请求异常')

# url='https://jsonplaceholder.typicode.com/users'
#
# response=requests.get(url=url)
# response_data=response.json()
# print(response_data)
# for user in response_data:
#     print(user['name'])
#


url='https://jsonplaceholder.typicode.com/posts'
data={
    'title':'新内容',
    'body':'555555',
    'userid':'222'
}
response=requests.post(url=url,data=data)
response_data=response.json()
new_id=response_data['id']
print(response.json())
print(new_id)
