# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from Task_1 import delsymbol
import doctest


def test_def():
    '''
    >>> delsymbol('hello')
    'hello'
    >>> delsymbol('Hello')
    'hello'
    >>> delsymbol('hello, world')
    'hello world'
    >>> delsymbol('hello мир')
    'hello '
    >>> delsymbol('Hello, мир')
    'hello '
    '''


if __name__ == '__main__':
    test_def()
    doctest.testmod(verbose=True)
