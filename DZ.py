# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.
# -------------------------------------------------------------------------------------------------
# # Создайте функцию генератор чисел Фибоначчи
import doctest
import unittest
import pytest


def fibon(number):
    if number > 2:
        fibo = [0, 1]
        for i in range(0, number - 1):
            sum_numbers = fibo[i] + fibo[i + 1]
            fibo.append(sum_numbers)
        return fibo
    else:
        return 'Access denied'

"""Док-тесты"""
# def tests_doc():
#     '''
#     >>> fibon(5)
#     [0, 1, 1, 2, 3, 5]
#     >>> fibon(-2)
#     'Access denied'
#     '''

"""Юнит-тесты"""
# class TestUnit(unittest.TestCase):
#     def test_positive_number(self):
#         self.assertEqual(fibon(5), [0, 1, 1, 2, 3, 5])
#
#     def test_negative_number(self):
#         self.assertEqual(fibon(-2), "Access denied")

"""Пай-тесты"""
def test_positive_number():
    assert fibon(5), [0, 1, 1, 2, 3, 5]


def test_negative_number():
    assert fibon(2), "Access denied"

# if __name__ == '__main__':
# tests_doc()
# doctest.testmod(verbose=True)
# unittest.main(verbosity=2)
