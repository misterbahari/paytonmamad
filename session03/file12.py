list1 = ['ali', 23, False, 'iran', 23, 35, 567, 23, 'ali', 'gg']
#print(list1)
#print(list1.count('ali'))
second_list = list1.copy()    #shallow copy
#print(second_list)
#print(id(list1))
#print(id(second_list))

third_list = list1     #deep_copy

#print(id(list1))
#print(id(third_list))


list1.append('dgdgj')
print(list1)

#list1.pop()
#print(list1)


#list1.reverse()
#print(list1)


list1.insert(4,'fati')
print(list1)

list1.remove('iran')
print(list1)


#list1.sort()
#print(list1)

list1 = []
list1.clear()
print(list1)