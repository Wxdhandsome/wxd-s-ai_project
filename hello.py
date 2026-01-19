# age=18
# if age>=18:
#     print("已成年")

# #if语句
# score=85
# if score>=90:
#     print("优秀")
# elif score>=80:
#     print("良好")
# elif score>=70:
#     print("及格")
# else:
#     print("不及格")


#whlie循环
# i=0
# while i <5:
#     print(f'第{i}次执行：')
#     print('hello,world')
#     print(i)
#     i+=1


# total=0
# for i in range(1,101):
#     total+=i
# print( total)
#
# count=0
# for i in range(2,501):
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             break
#     else:
#         print(i)
#         count+=1
# print(count)

i=int(input("请输入数字："))
if i%2==0:
    print(f'{i}是偶数')
else:
    print(f'{i}是奇数')


total=0
for i in range(1,101):
    total+=i
print(f'1到100的和为{total}')


list=[1,2,3,4,5]
print(list[::-1])

