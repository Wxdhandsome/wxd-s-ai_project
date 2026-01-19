class Account:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance += amount
        print(f'存款成功，余额为{self.balance}')
    def withdraw(self,amount):
        if amount > self.balance:
            print('余额不足')
        else:
            self.balance -= amount
            print(f'取款成功，余额为{self.balance}')
    def get_balance(self):
        return self.balance

# account_1=Account('1',1000)
# account_1.deposit(500)
# account_1.withdraw(200)
# print(account_1.get_balance())

class Bank:
    def __init__(self):

        self.accounts={}
    def create_account(self,account_number,balance):
        if account_number in self.accounts:
            return '账户已存在'
        self.accounts[account_number]=balance
        return f'账户创建成功,余额为{balance}'
    def get_account(self,account):
        account=input('请输入要查询的账号：')
        if account in self.accounts:
            return self.accounts[account]
        else:
            return '账户不存在'
    def transfer(self,account_1,account_2,amount):
        if account_1 in self.accounts and account_2 in self.accounts:
            if self.accounts[account_1] >= amount:
                self.accounts[account_1] -= amount
                self.accounts[account_2] += amount
                return '转账成功'
            else:
                return '余额不足'
        else:
            return '账户不存在'
bank=Bank()
account_1=bank.create_account(account_number=1,balance=500)
account_2=bank.create_account(account_number=2,balance=500)
print(bank.get_account(1))
print(bank.transfer(1,2,100))
print(bank.get_account(2))