class Gun:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.number = 0

    def get_number(self):
        return self.number

    def reload(self):
        self.number += 1

    def shoot(self, auto=False):
        if self.number == 0:
            print('reloaaaaaaaaaaaaaaaaaad plz')
        if auto == 'manual' or auto == False:
            self.number -= 1
        else:
            self.number -= 5

ak47 = Gun('ak47')

print(ak47.get_number())
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
ak47.reload()
print(ak47.get_number())

ak47.shoot()
print(ak47.get_number())


ak47.shoot(auto=True)
print(ak47.get_number())

print(42 - 37)
