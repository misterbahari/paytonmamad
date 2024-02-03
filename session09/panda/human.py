class Human():
    def __init__(self, name):
        self.name = name
        self.say_name()

    def say_name(self):
        print(f'human name is {self.name}')