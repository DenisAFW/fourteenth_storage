# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from Task_1 import delsymbol
import unittest


class TestUnit(unittest.TestCase):
    def test_method(self):
        self.assertEqual(delsymbol('hello world'), 'hello world')

    def test_lower(self):
        self.assertEqual(delsymbol('Hello World'), 'hello world')

    def test_symbol(self):
        self.assertEqual(delsymbol('Hello, world'), 'hello world')

    def test_language(self):
        self.assertEqual(delsymbol('Hello Мир'), 'hello ')

    def test_all(self):
        self.assertEqual(delsymbol('Hello, мир'), 'hello ')


if __name__ == '__main__':
    unittest.main(verbosity=2)
