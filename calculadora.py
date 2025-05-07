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

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


# def soma(x, y, z):
#     assert isinstance(x, (int, float)), 'x precisa ser int ou float'
#     assert isinstance(y, (int, float)), 'y precisa ser int ou float'
#     assert isinstance(z, (int, float)), 'z precisa ser int ou float'
#     return x + y + z