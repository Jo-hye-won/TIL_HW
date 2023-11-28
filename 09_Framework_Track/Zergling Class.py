class Zergling :
    def __init__(self):
        self.hp = 80
        self.mana = 200

    def attack(self):
        self.hp += 1
        self.mana -= 10

    def move(self):
        self.hp -= 10
        self.mana += 5

    def status(self):
        print(self.hp)
        print(self.mana)


t = Zergling()

print(t.attack())
print(t.move())
print(t.status())