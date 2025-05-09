import unittest
from calculadora import *

class TestCalculadora(unittest.TestCase):
    def test_soma_banco(self):
        bancos = (
            (2, 5, 7),
            (5, 5, 10),
        )
        for banco in bancos:
            with self.subTest(banco=banco):
                x, y, resultador = banco
                self.assertEqual(casa(x, y), resultador)

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

    def test_soma_k_a(self):
        k_a_saidas = (
            (12, 15, 27),
            (10, 10, 20),
            (15, 15, 30),
        )
        for k_a_saida in k_a_saidas:
            with self.subTest(k_a_saida=k_a_saida):
                k, a, saida = k_a_saida
                self.assertEqual(testando_conhecimento_sozinho(k, a), saida)

    # Subtrai -> outra funçao da Calculadora...
    def test_subtrai_5_5_resoltador_e_0(self):
        self.assertEqual(subtrai(5, 5), 0)
    
    def test_varios_test_subtrai(self):
        a_b_resultador = (
            (5, 5, 0),
            (15, 5, 10),
            (50, 50, 0),
            (8, 5, 3),
        )
        for a_b_resultado in a_b_resultador:
            with self.subTest(a_b_resultado=a_b_resultado):
                a, b, resultado = a_b_resultado
                self.assertEqual(subtrai(a, b), resultado)

    def test_soma_x_nao_e_int_ou_float_deve_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)

    def test_soma_y_nao_e_int_ou_float_deve_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(4, '5')

    def test_soma(self):
        self.assertEqual(testando_conhecimento_sozinho(5, 5), 10)

    def test_contas_resolver(self):
        self.assertEqual(contas(5, 5), 10)

    def test_dividindo_salarios(self):
        self.assertEqual(dividindo_os_valores_do_salarios(100, 2), 50)

    def test_somando_as_funcao_dos_tres_valores(self):
        self.assertEqual(somando_tres_valores(10, 10, 10), 30)

    def test_multiplica_o_valor(self):
        self.assertEqual(multiplica(2, 5), 10)

    def test_casa_somando_valor_x_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            casa('5', 5)

    def test_sasa_valor_y_error(self):
        with self.assertRaises(AssertionError):
            casa(5, '5')

    def test_dividindo_os_valores_do_salarios(self):
        self.assertEqual(dividindo_os_valores_do_salarios(5, 2), 2.5)

    # Testando os errors do assert a e b
    def test_dividindo_achando_error_a(self):
        with self.assertRaises(AssertionError):
            dividindo_os_valores_do_salarios('4', 4)
    
    def test_dividindo_achando_errors_b(self):
        with self.assertRaises(AssertionError):
            dividindo_os_valores_do_salarios(5, '4')

    # Testando os erros dos tres valores a, b e c
    def test_somando_tres_valores_erro_a(self):
        with self.assertRaises(AssertionError):
            somando_tres_valores('4', 5, 5)

    def test_somando_tres_valores_errors_b(self):
        with self.assertRaises(AssertionError):
            somando_tres_valores(5, '4', 5)

    # Multiplica os valores 
    def test_multiplica(self):
        valores = (
            (5, 5, 25),
            (2, 5, 10),
        )
        for valore in valores:
            with self.subTest(valore=valore):
                a, b, valore = valore
                self.assertEqual(multiplica(a, b), valore)

unittest.main(verbosity=2)