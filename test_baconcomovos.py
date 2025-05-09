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

class TestBaconComOvos(unittest.TestCase):
    # 1 -> Teste ele retorna o erro da função AssertionError
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')

    #2 -> Teste ser o numero é multiplo de 3 e 5
    # def test_bacon(self):    -> Testei esse código so para sab sobre um teste só
    #     self.assertEqual(bacon_com_ovos(15), 'Bacon com ovos')
    def test_bacon_com_ovos_deve_retorna_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30)
        saida = "Bacon com ovos"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retorna "{saida}"'
                )

    #3 -> Teste ser não é multiplos de 3 e 5
    def test_bacon_com_ovos_deve_retorna_passa_fomer_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = "Passa fomer"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retorna "{saida}"'
                )
    
    #4 -> Test ser a entrada for multiplo de 3
    def test_bacon_com_ovos_deve_retorna_Bacon_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = "Bacon"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retorna "{saida}"'
                )
    
    #5 -> Test ser a entrada for multiplo de 5
    def test_bacon_com_ovos_deve_retorna_Bacon_se_entrada_for_multiplo_de_5(self):
        entradas = (50, 55, 65, 70)
        saida = "Ovos"

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada), saida, msg=f'"{entrada}" não retorna "{saida}"'
                )

unittest.main(verbosity=2)