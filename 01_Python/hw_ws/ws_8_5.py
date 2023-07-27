# ws_8_5.py
class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.num_of_animal += 1
        

# Dog클래스와 Cat클래스는 각각 sound클래스 속성을 가지며,
# 각동물의 소리를 나타낸다.        
class Dog(Animal):
    sound = '멍멍'

class Cat(Animal):
    sound = '야옹'

# Pet클래스는 Dog클래스와 Cat클래스를 다중 상속받아야 한다.
class Pet(Dog, Cat):

    def __init__(self, sound):
        Animal.__init__(self)
        self.sound = sound
        

    def play(self):
        print('애완동물과 놀기')

    def make_sound(self):
        print(self.sound)

 # 오버라이딩 : 재정의하는 것 : dust= 50 / dust=60 => dust=60(재할당 했음)
    @classmethod
    def __str__(cls):
        return f'애완동물은 {cls.sound} 소리를 냅니다.'


pet1 = Pet("멍")
print(pet1)