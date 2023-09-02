# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest

from Rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_1_area(self):
        self.assertEqual(Rectangle.get_area(Rectangle(2)), 4)

    def test_2_perimetr(self):
        self.assertEqual(Rectangle.get_perimetr(Rectangle(2, 5)), 14)

    def test_3_sub(self):
        self.assertEqual(str(Rectangle(3, 7) - Rectangle(2, 5)), str(Rectangle(1, 2)))

    def test_4_sum(self):
        self.assertEqual(str(Rectangle(5, 5) + Rectangle(10, 10)), str(Rectangle(15, 15)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
