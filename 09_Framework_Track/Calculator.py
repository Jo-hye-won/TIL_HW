class Calculator:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.result = 0

    def plus(self):
        self.result = self.a + self.b
        return self.result

    def minus(self):
        self.result = self.a - self.b
        return self.result

    def divide(self):
        self.result = self.a // self.b
        return self.result

    def multiple(self):
        self.result = self.a * self.b
        return self.result

    def _printResult(self):
        print(self.result)


a = Calculator()
a.a = 1
a.b = 2
a.plus()
a.multiple()
a.divide()

a._printResult()