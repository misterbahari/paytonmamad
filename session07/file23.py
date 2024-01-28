#def test(name):
    #print(name)

#test('ali')


def test(*args):
    print(args)

test(2,4,5,67,8)


def gigi(**kwargs):
    print(kwargs)

gigi(name='ali',family='rezaie')



def lala(*args,**kwargs):
    print(args)
    print(kwargs)

lala(2,3,4,5,6,7,78,'ali',[2,4,5,66],name='reza')