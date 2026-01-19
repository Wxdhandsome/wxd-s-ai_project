class Chararter:
    def __init__(self,name,health,attack_power):
        self.name=name
        self.health=health
        self.attack_power=attack_power
    def attack(self,target):
        pass
    def is_live(self,target):
        pass

class Warrior(Chararter):
    def __init__(self,armor,name,health,attack_power,physical_attack):
        super().__init__(name,health,attack_power)
        self.armor=armor
        self.physical_attack=physical_attack
    def attack(self,target):
        target.health =target.health - self.attack_power -self.physical_attack
    def is_live(self,target):
        if self.health > 0:
            return f'{self.name}还活着,{self.name}剩余生命值{self.health}'
        else:
            return '死了'


class Mage(Chararter):
    def __init__(self,mana,name,health,attack_power,magical_attack):
        super().__init__(name,health,attack_power)
        self.mana=mana
        self.magical_attack=magical_attack
    def attack(self,target):
        target.health=target.health - self.attack_power + target.armor
    def fireball(self,target):
        if self.mana >=10:
            target.health= target.health - self.magical_attack -self.attack_power + target.armor
        else:
            print('魔法值不足')
        self.mana -= 10
    def is_live(self, target):
        if self.health > 0:
            return f'{self.name}还活着,{self.name}剩余生命值{self.health}'
        else:
            return '死了'


warrior=Warrior(10,'战士',100,10,5)
mage=Mage(20,'法师',100,10,10)
print('战士攻击了法师')
warrior.attack(mage)
print(mage.is_live(mage))
print('法师使用了火球术')
mage.fireball(warrior)
print(warrior.is_live(warrior))