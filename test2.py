def cir_sq(r):
    return 3.14*r**2
r=float(input("请输入半径："))
print(f'圆的面积为{cir_sq(r):.2f}')

import datetime
def year():
    now=datetime.datetime.now().year
    if now%4==0 and now%100!=0 or now%400==0:
        print('闰年')
    else:
        print('平年')
year()

list=[1,2,3,4,5]
with open('numbers.txt','w',encoding='utf-8') as f:
    for i in list:
        f.write(str(i))
        f.write('\n')

list2=[]
with open('numbers.txt','r',encoding='utf-8') as f2:
    while True:
        line=f2.readline()
        if not line:
            break
        else:
            line=line.strip()
            list2.append(int(line))
print(f'平均值为：{sum(list2)/len(list2)}')


import password_generator
length=int(input('请输入密码长度：'))
pwd=password_generator.password_generator(length)
print(pwd)
