class Robot:
    def __init__(self):
        self.hp = 0

    def move(self):
        pass

    def stop(self):
        pass

class SpeedRobot(Robot):
    def __init__(self):
        super().__init__()
        self.modelID: 0

    def run(self):
        pass

    def walk(self):
        pass

class PowerRobot(Robot):
    def __init__(self):
        super().__init__()
        self.mana: 0


    def attack(self):
        pass

    def jump(self):
        pass

a = SpeedRobot()
print(a.hp)