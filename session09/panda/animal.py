class Animal():
    def __init__(self, name):
        self.name = name
        self.say_name()

    def say_name(self):
        print(f'animal name is {self.name}')