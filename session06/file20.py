from itertools import cycle

list_var = ['reza', 'mahdi', 'hamid']
list_var = iter(list_var)
print(list_var.__next__())
print(list_var.__next__())
print(list_var.__next__())

#list1 = ['aa','bb','cc']
#list1 = cycle(list1)
