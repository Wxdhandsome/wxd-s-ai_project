import random
import string
def password_generator(length):
    return ''.join(random.choice(string.ascii_letters+string.digits)for i in range(length))
if __name__=='__main__':
    length = int(input('请输入密码长度：'))
    print(password_generator(length))
