class Dog:
    species = 'Canis lupus'
    dogs_count = 0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Dog.dogs_count += 1
    def bark(self):
        print(f"{self.name} is barking")
    @classmethod
    def get_species(cls):
        return cls.species
    @classmethod
    def get_count(cls):
        return cls.dogs_count
    @classmethod
    def create_puppy(cls,name):
        return cls(name,1)

my_dog=Dog('Max',5)
print(my_dog.name)
print('---------------------------------')
print(my_dog.age)
print('---------------------------------')
my_dog.bark()
print('---------------------------------')
print(Dog.get_count())
print(Dog.get_species())
print('---------------------------------')


puppy=Dog.create_puppy('Buddy')
print(f'{puppy.name} is a {puppy.age} year old dog')