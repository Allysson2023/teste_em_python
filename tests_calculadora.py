import unittest
from calculadora import *

class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retorna_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_negativo_5_deve_retorna_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (15, 15, 30),
            (40, 40, 80),
            (1, 1, 2),
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    # Subtrai -> outra funçao da Calculadora...
    # def test_subtrai_5_5_resoltador_e_0(self):
    #     self.assertEqual(subtrai(5, 5), 0)
    
    # def test_varios_test_subtrai(self):
    #     a_b_resultador = (
    #         (5, 5, 0),
    #         (15, 5, 10),
    #         (50, 50, 0),
    #         (8, 5, 3),
    #     )

    #     for a_b_resultado in a_b_resultador:
    #         with self.subTest(a_b_resultado=a_b_resultado):
    #             a, b, resultado = a_b_resultado
    #             self.assertEqual(subtrai(a, b), resultado)

    def test_soma_x_nao_e_int_ou_float_deve_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)

    def test_soma_y_nao_e_int_ou_float_deve_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(4, '5')


unittest.main(verbosity=2)