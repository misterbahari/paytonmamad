class MyRange:
    def __init__(self, start, stop):
        self.start = start
        self.current = start
        self.end = stop

    def __iter__(self):
        return self

    def __next__(self):

        if self.current < self.end:
            self.current += 1
            return self.current - 1

        else:
            raise StopIteration('khata darad baradar')


my_range = MyRange(1, 6)
print(my_range.__next__())
print(my_range.__next__())
print(my_range.__next__())
print(my_range.__next__())
print(my_range.__next__())


for item in MyRange(1,100):
    print(item)

for i in range(10):
    print(i)