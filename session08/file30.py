class Animal:
    def say_hi(self):
        return "HI"

    def say_bye(self, counter):
        return "bye" * counter

    def test(self):
        self.color = 'pink'
        return None

zebra_one = Animal()
# res_hi= zebra_one.say_hi()
# print(res_hi)
#
# res_bye = zebra_one.say_bye(5)
# print(res_bye)

test = zebra_one.test()
print(test)