import math

adad = (input('adad bede be man').split())
len1 = len(adad)
numbers_str_list = adad
numbers_int_list = list(map(float , adad))
avg = sum(numbers_int_list) / len1
avg2 = math.ceil(avg)
print(avg2)
print(avg)




#print(type(numbers_str_list[0]))
#print(type(numbers_int_list))
#print(numbers_str_list)

