# Test com unitarios com -> TDD

"""
1 - Receber um numero inteiro
2 - Saber se o numero é multiplo de 3 e 5:
    Bacon com ovos
3 - Saber ser o numero NÃO é multiplo de 3 e 5:
    Passa fome
4 - Saber se o numero é multiplo somente de 3:
    Bacon
5 - Saber se o numero é multiplo somente de 5:
    Ovos
"""

def bacon_com_ovos(n):
    assert isinstance(n, int), 'o valor N dever ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    
    if n % 3 == 0:
        return 'Bacon'
    
    if n % 5 == 0:
        return 'Ovos'
    
    return 'Passa fomer'