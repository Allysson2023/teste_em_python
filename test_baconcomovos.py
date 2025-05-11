"""
TDD -> Test driven development (Desenvolvimento dirigido a testes)

RED
Parte 1 -> Criar o teste e ver falhar

GREEN
Parte 2 -> Criar o código e ver o teste passar

REFACCTOR
Parte 3 -> Melhorar meu código

"""

import unittest
from bacon_com_ovos import *

# class TestBaconComOvos(unittest.TestCase):
#     # 1 -> Teste ele retorna o erro da função AssertionError
#     def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
#         with self.assertRaises(AssertionError):
#             bacon_com_ovos('')

#     #2 -> Teste ser o numero é multiplo de 3 e 5
#     # def test_bacon(self):    -> Testei esse código so para sab sobre um teste só
#     #     self.assertEqual(bacon_com_ovos(15), 'Bacon com ovos')
#     def test_bacon_com_ovos_deve_retorna_se_entrada_for_multiplo_de_3_e_5(self):
#         entradas = (15, 30)
#         saida = "Bacon com ovos"

#         for entrada in entradas:
#             with self.subTest(entrada=entrada, saida=saida):
#                 self.assertEqual(
#                     bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retorna "{saida}"'
#                 )

#     #3 -> Teste ser não é multiplos de 3 e 5
#     def test_bacon_com_ovos_deve_retorna_passa_fomer_se_entrada_nao_for_multiplo_de_3_e_5(self):
#         entradas = (1, 2, 4, 7, 8)
#         saida = "Passa fomer"

#         for entrada in entradas:
#             with self.subTest(entrada=entrada, saida=saida):
#                 self.assertEqual(
#                     bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retorna "{saida}"'
#                 )
    
#     #4 -> Test ser a entrada for multiplo de 3
#     def test_bacon_com_ovos_deve_retorna_Bacon_se_entrada_for_multiplo_de_3(self):
#         entradas = (3, 6, 9, 12, 18, 21)
#         saida = "Bacon"

#         for entrada in entradas:
#             with self.subTest(entrada=entrada, saida=saida):
#                 self.assertEqual(
#                     bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retorna "{saida}"'
#                 )
    
#     #5 -> Test ser a entrada for multiplo de 5
#     def test_bacon_com_ovos_deve_retorna_Bacon_se_entrada_for_multiplo_de_5(self):
#         entradas = (50, 55, 65, 70)
#         saida = "Ovos"

#         for entrada in entradas:
#             with self.subTest(entrada=entrada, saida=saida):
#                 self.assertEqual(
#                     bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retorna "{saida}"'
#                 )


# class TestCarro(unittest.TestCase):
    # Verificando ser o c é int ou float
    # def test_verificando_ser_o_carro_e_int_ou_float(self):
    #     with self.assertRaises(AssertionError):
    #         carro_no_estacionamento('')

    # # Verificando ser o pagamento é no valor certo...
    # def test_pagemento_do_estacionamento_valor_5(self):
    #     self.assertEqual(carro_no_estacionamento(5), 'Pagamento efetuado com sucesso!')

    # # Verificando quando o pagamento for pago ele pode sair (Valor 1 = Não pagou, Valor 2 = Cancela levantada)
    # def test_saindo_do_estacionamento_depois_que_efetuou_pagamento_5(self):
    #     self.assertEqual(carro_no_estacionamento(2), 'Cancela de sair levantada com sucesso!')

# class TestEstacionamento(unittest.TestCase):

#     def test_pagamento_tipo_invalido(self):
#         with self.assertRaises(AssertionError):
#             efetuar_pagamento('fd')
    
#     def test_pagemento_com_valor_insuficiente(self):
#         self.assertEqual(efetuar_pagamento(3), "Voce tem que pagar o estacionamento!")

#     def test_pagamento_com_valor_exato(self):
#         self.assertEqual(efetuar_pagamento(5), "Pagamento efetuado com sucesso!")

#     def test_saida_do_pagamento(self):
#         self.assertEqual(sair_do_estacionamento(True), "Cancela de saida levantada com sucesso!")

#     def test_saida_do_pagamento_nagada(self):
#         self.assertEqual(sair_do_estacionamento(False), "Pagamento necessário antes de sair.")


class Test_nota_aluno(unittest.TestCase):
    def test_ser_a_nota_e_int_ou_float(self):
        with self.assertRaises(AssertionError):
            nota_aluno('')
    
    def test_ser_a_nota_e_maio_que_7(self):
        self.assertEqual(nota_aluno(7), 'o aluno está Aprovado.')

    def test_ser_a_nota_e_valida(self):
        self.assertEqual(nota_aluno(-1), "Nota inválida")

    def test_ser_a_nota_e_menor_que_a_media_7(self):
        self.assertEqual(nota_aluno(4), 'o aluno está Reprovado.')

unittest.main(verbosity=2)