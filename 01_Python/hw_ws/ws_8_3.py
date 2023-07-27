# ws_8_3.py
class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.num_of_animal += 1

# 아래 클래스를 수정하시오.
class Cat(Animal):
   def meow(self):
       print('야옹!')

cat1 = Cat()
cat1.meow()