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

"""
Exercicio que eu que fiz sozinho

Crie uma função que simule o processo de entrada e saída de um carro em um estacionamento de um comércio.

Regras:

O valor recebido pela função deve ser do tipo int ou float. Caso contrário, deve gerar um erro.

Para sair do estacionamento, o cliente deve pagar R$ 5,00.

Após o pagamento correto, a função deve permitir a saída do carro, simulando a abertura da cancela.

"""

# def carro_no_estacionamento(c) -> int:
    # Verificando ser é int ou float
    # assert isinstance(c, (int, float)), ' O carro dever ser int ou float'
    
    # Verificando ser pagamento é maior ou igual a 5
    # if c >= 5:
    #     return "Pagamento efetuado com sucesso!"

    # Verificando valor 1 = Não pagou, valor 2 = A cancela levanta 1 e 2 sao código de pagamento que eu que criei
    # if c == 2:
    #     return 'Cancela de sair levantada com sucesso!'
    
    # Ser o pagamento for menor doque o valor não é pago e nem pode sair do estacionamento
    # return "Voce tem que pagar o estacionamento!"

# Funçao para efetuar o pagamento -> chat

def efetuar_pagamento(valor) -> str:
    assert isinstance(valor, (int, float)), 'o valor deve ser int ou float'

    if valor >= 5:
        return "Pagamento efetuado com sucesso!"
    return "Voce tem que pagar o estacionamento!"

def sair_do_estacionamento(pagamento:bool) -> str:
    
    if pagamento:
        return "Cancela de saida levantada com sucesso!"
    return "Pagamento necessário antes de sair."




# ✅ Regras:
# A nota deve ser obrigatoriamente do tipo int ou float. ok

# Se a nota for maior ou igual a 7.0, o aluno está Aprovado. ok

# Se a nota for menor que 7.0, o aluno está Reprovado. ok

# Se a nota for de tipo inválido (como string, lista, etc), deve lançar um erro. ok

# Se a nota for menor que 0 ou maior que 10, deve mostrar "Nota inválida".

def nota_aluno(nota: int | float):
    assert isinstance(nota, (int, float)), 'A nota do Aluno dever ser int ou float'
    
    if nota < 0 or nota > 10:
        return "Nota inválida"

    if nota >= 7.0:
        return 'o aluno está Aprovado.'
    
    return 'o aluno está Reprovado.'

print(nota_aluno(7))