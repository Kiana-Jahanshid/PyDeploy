


def test():
    yield 1
    yield 2
    yield 3


for value in test():
    print(value)


'''
output :
in first iter  : 1
in second iter : 2
in third iter : 3

yield works like return But  :
after running return , none of the next following lines will be executed .
but in yield 
at first it return 1 , then it allows another next lines to be executed .


'''