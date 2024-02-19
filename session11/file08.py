#double inheritance
class Wildanimal:
    def speak(self):
        print('wow')

    def eat(self):
        print('i am eating')

class Animal:
    def speak(self):
        print('jik jik')


class Dog(Animal, Wildanimal):
    def speak(self):
        print('man daram harf mizanam')



huski = Dog()
huski.eat()
huski.speak()
