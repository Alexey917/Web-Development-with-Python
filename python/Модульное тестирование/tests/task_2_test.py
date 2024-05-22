import unittest
import task_2


class MyTest(unittest.TestCase):
    def test_write(self):
        self.assertEqual(task_2.number.path, 'number.txt')

    def test_conversion_oct(self):
        self.assertEqual(task_2.number.conversion(task_2.number.oct), '55')

    def test_conversion_hex(self):
        self.assertEqual(task_2.number.conversion(task_2.number.hex), '2D')

    def test_conversion_bin(self):
        self.assertEqual(task_2.number.conversion(task_2.number.bin), '101101')


if __name__ == '__main__':
    unittest.main()


