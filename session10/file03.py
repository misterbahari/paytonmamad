class WildAnimal(object):
    is_wild = True
    category = 'wild'

    @classmethod
    def eat_meat(cls):
        cls.category = 'vahshi'
        return 'animal is eating meat and category is ' + cls.category


    def say_hi(self):
        self.category = 'sag sanan'
        return 'wowwww'


    @staticmethod
    def get_age(age):
        if age > 18:
            print('over 18')
        else:
            print('lower 18')



# sarabi = WildAnimal()

# print(WildAnimal.is_wild)
# print(WildAnimal.category)
# print(WildAnimal.eat_meat())
#
# # print(sarabi.say_hi())
#
# print(WildAnimal().say_hi())

huski = WildAnimal()

print(huski.say_hi())

huski.get_age(15)