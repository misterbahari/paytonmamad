class tofangk:
    def __init__(self):
        self.tedad = 50

    def taktir(self):
        if self.tedad >= 1:
            self.tedad -= 1
            return self.tedad
        else:
            print("nmishe")

    def ragbar(self):
        if self.tedad >= 5:
            self.tedad = self.tedad - 5
            return self.tedad
        else:
            print("nimshe")


tof = tofangk()
print(tof.ragbar())
