def my_decorator(function):
    def internal_function(*args,**kwargs):
        print('salam')
        res = function(*args, **kwargs)
        print('bye')
        return res * 2
    return internal_function
@my_decorator
def saam(a,b):
    print('saaaaaaaaaaaaaaaaaaaaaaaaam')
    return a + b

@my_decorator
def paawer(a, b):
    print('paaaaaaaaawer')
    return a ** b




res = saam(2,5)
print(res)

res2 = paawer(2,6)
print(res2)