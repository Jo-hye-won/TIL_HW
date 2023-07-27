# ws_8_1.py

# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.increase_number()
    
    @classmethod
    def increase_number(cls):
        Animal.num_of_animal += 1
        
class Dog(Animal):
    def __init__(self):
        super().__init__()

class Cat(Animal):
    def __init__(self):
        super().__init__()

class Pet(Dog, Cat):
    def access_num_of_animal():
        return f'동물의 수는 {Animal.num_of_animal}마리 입니다.'


dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())

