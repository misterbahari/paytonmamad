class Human(object):
    def __init__(self, name, family):
        self.name = name
        self.family = family
        self.hair = None
        self.age = 1
        self.hi_mom()

    def hi_mom(self):
        print('hi mo mo!')

    def set_color(self, color='black'):
        self.color = color
        print(color)




bardia = Human('bardia', 'razavi')
res = bardia.age
res2 = bardia.hair
print(res)
print(res2)

#res3 = bardia.hi_mom()
# print(res3)

res4 = bardia.set_color()
print(res4)

