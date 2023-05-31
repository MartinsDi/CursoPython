import sys
# Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']

iterator = iterable.__iter__() # tem __iter__ e __next__
iterator = iter(iterable) # mesmo resultado da linha anterior


lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))
gen = (i for i in iterable)
gen2 = [i for i in iterable]

#print(iterator)
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))

'''print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
print(sys.getsizeof((gen)))
print(sys.getsizeof((gen2)))'''

'''def generator(n=0):
    yield 1
    return 'ACABOU' '''


def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return

'''gen = generator(n=0)
for n in gen:
    print(n)'''

# Yield from
def gen1():
    yield 1
    yield 2
    yield 3

def gen2( ):
    yield from gen1()
    yield 4
    yield 5
    yield 6


g = gen2()
for i in g:
    print(i)


