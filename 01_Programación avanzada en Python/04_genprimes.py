from collections.abc import Iterator, Callable
from typing import Iterator, TypeVar

T = TypeVar('T')

def all_natural_numbers() -> Iterator[int]:
    """
    generator of all natural numbers

    """
    n = 0
    while True:
        yield n
        n += 1

def test_all_natural_numbers():
    g = all_natural_numbers()
    assert [next(g) for _ in range(10)] == list(range(10))
    print('OK')

def div(p: int) -> Callable[[int], bool]:
    '''
    This functions returns anothe function that depends on the parameter p.
    The returned function checks if certain number is divisble by p or not.
    '''
    return lambda x: x % p != 0


def test_div():
    f = div(10)
    assert not f(100), f'{f(100)}'
    assert not f(10)
    for i in range(1, 10):
        assert  f(i)
    print('OK')


def gen_primes() -> Iterator[int]:
    '''
    This function is an iterator of all prime numbers.
    It a lazy version of the 'Sieve of Eratosthenes'
    (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
    '''
    candidates = filter(lambda x: x>1, all_natural_numbers())
    while True:
        prime = next(candidates)
        yield prime
        candidates = filter(div(prime), candidates)


def test_gen_primes():
    p = gen_primes()
    l = [ next(p) for _ in range(10)]
    assert l == [2, 3 , 5, 7, 11, 13, 17, 19, 23, 29], f'{str(l)}'
    print('OK')



class LazyList:
    '''
    This class allows us to us an 'infinite' iterator like the iterator
    of all numbers or the iterator of all primes as an ordinay list.
    '''
    @staticmethod
    def getmaxslice(p: slice) -> int:
        if p.step is None or p.step > 0:
            last = p.stop
        else:
            last = p.start
            if last is None:
                raise Exception('Cannot get all ellements of the iterator')
        return last

    def __init__(self, iter: Iterator[T]):
        self.__data = []
        self.__iter = iter

    def __getitem__(self, pos) -> T:
        if isinstance(pos, int):
            if pos<0:
                raise IndexError(f'Negative position {pos} is illegal')
            self.__data.extend([next(self.__iter)
                                for _ in range(len(self.__data), pos+1)])
        else:
            last = self.getmaxslice(pos)
            self.__data.extend([next(self.__iter)
                                for _ in range(len(self.__data), last+1)])
        return self.__data[pos]

def test_LayzyList():
    nat = LazyList(all_natural_numbers())
    assert nat[100] == 100
    assert nat[:100] == list(range(100)), f'{nat[:100]}'

    p = LazyList(gen_primes())
    assert p[0] == 2
    assert p[:10] == [2, 3 , 5, 7, 11, 13, 17, 19, 23, 29], f'{p[:10]}'
    print('OK')

# def gen_prime_lst_1(upto: int) -> list:
#     l = filter(lambda x: x>1, all_natural_numbers())
#     plst = []
#     cont = True
#     while cont:
#         p = next(l)
#         if p > upto:
#             cont = False
#         else:
#             plst.append(p)
#             l = filter(div(p), l)
#     return plst


# def gen_prime_lst_2(upto: int) -> list:
#     l = filter(lambda x: x>1, all_natural_numbers())
#     plst = []
#     cont = True
#     while cont:
#         p = next(l)
#         if p > upto:
#             cont = False
#         else:
#             plst.append(p)
#             l = filter(lambda x: x % p != 0, l)
#     return plst
