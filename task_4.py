# Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)
from Task_1 import delsymbol
import pytest


def test_method():
    assert delsymbol('hello world'), 'Что-то не так'


def test_lower():
    assert delsymbol('Hello World'), 'Буквы все также заглавные'


def test_symbol():
    assert delsymbol('Hello, world'), 'Знаки препинания не пропали'


def test_language():
    assert delsymbol('Hello Мир'), 'Другие языки не пропадают'


def test_all():
    assert delsymbol('Hello, мир'), 'Все выше перечисленные проверки провалены'
