# Test em Python

def soma(x, y):
    """ Soma x e y
    >>> soma(10, 20)
    30

    >>> soma(10, 10)
    20

    >>> soma('10', 10)
    Traceback (most recent call last):
    ...
    AssertionError: x precisa ser int ou float
  
    """

    assert isinstance(x, (int, float)), 'x precisa ser int ou float'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float'
    return x + y

def subtrai(a, b):
    """ Subtrair a e b

    >>> subtrai(10, 5)
    5
    
    >>> subtrai('10', 5)
    Traceback (most recent call last):
    ...
    AssertionError: a precisa ser int ou float

    >>> subtrai(49, '10')
    Traceback (most recent call last):
    ...
    AssertionError: b precisa ser int ou float


    """
    assert isinstance(a, (int, float)), 'a precisa ser int ou float'
    assert isinstance(b, (int, float)), 'b precisa ser int ou float'
    return a - b

def somab(c, d):
    """ Somab c e b
    >>> somab(15, 15)
    30

    >>> somab('15', 10)
    Traceback (most recent call last):
    ...
    AssertionError: c Precisa ser int ou float

    """
    assert isinstance(c, (int, float)), 'c Precisa ser int ou float'
    assert isinstance(d, (int, float)), 'd Precisa ser int ou float'
    return c + d

def testando_conhecimento_sozinho(k, l):
    """Testando k e l:
    >>> testando_conhecimento_sozinho('5', 5)
    Traceback (most recent call last):
    ...
    AssertionError: O valor K tem que ser int ou float

    """

    assert isinstance(k, (int, float)), 'O valor K tem que ser int ou float'
    assert isinstance(l, (int, float)), 'O valor L tem que ser int ou float'

    return k + l


def casa(x, y):
    assert isinstance(x, (int, float)), "o valor de X deve ser int ou float"
    assert isinstance(y, (int, float)), "o valor de Y deve ser int ou float"
    return x + y

def contas(x, y):
    assert isinstance(x, (int, float)), "o valor X deve ser int ou float"
    assert isinstance(y, (int, float)), "o valor Y deve ser int ou float"
    return x + y
 
def dividindo_os_valores_do_salarios(a, b):
    """ dividi
    >>> dividindo_os_valores_do_salarios(5, 2)
    2.5
    """
    assert isinstance(a, (int, float)), "o valor A tem que ser int ou float"
    assert isinstance(b, (int, float)), "o valor B tem que ser int ou float"
    return a / b

def somando_tres_valores(a, b, c):
    """ Soma de tres valores
    >>> somando_tres_valores(5, 5, 5)
    15
    """
    assert isinstance(a, (int, float)), "o valor de A deve ser int ou float"
    assert isinstance(b, (int, float)), "o valor de B deve ser int ou float"
    assert isinstance(c, (int, float)), "o valor de C deve ser int ou float"
    return a + b + c

def multiplica(x, y):
    """Multiplica dois números."""
    assert isinstance(x, (int, float)), "x deve ser int ou float"
    assert isinstance(y, (int, float)), "y deve ser int ou float"
    return x * y

# def soma(x, y, z):
#     assert isinstance(x, (int, float)), 'x precisa ser int ou float'
#     assert isinstance(y, (int, float)), 'y precisa ser int ou float'
#     assert isinstance(z, (int, float)), 'z precisa ser int ou float'
#     return x + y + z

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)