class Animal(object):
    def __init__(self, name, age):


        self.name = name
        self.age = age
        #print(name)
        #print(age)
    def sleep(self):
        return 'zzzzzzzzzzzzz'

    def speak(self):
        pass

    def eat(self):
        print('eating')

class Zarrafe(Animal):
    def __init__(self, category, **kwargs):
        super().__init__(**kwargs)
        self.category = category

        
    def eat(self, number):
        print('eat grass' * number)                      #overwrite

    def sleep(self):
        print(super().sleep() + 'khamiaze')                  #extend

    def speak(self):
        print('im speaking')                           #creating

#zizi = Zarrafe( name='zozo',category='wild', age=14)
#zizi.eat(3)
#zizi.sleep()
#zizi.speak()

class Dog(Animal):
    def speak(self):
        print('burk')

    def __str__(self):
        pass

dog_one = Dog('huski', age=15)
dog_one.speak()

class Wilddog(Dog):
    pass

wild_dog = Wilddog('dobberman', 20)
wild_dog.speak()
print(wild_dog.sleep())