import unittest
import task_1


class MyTest(unittest.TestCase):
    def test_sum_of_elem(self):
        self.assertEqual(task_1.sum_of_elem.sum_of_elem(), 1667)

    def test_mid(self):
        self.assertEqual(task_1.mid.mid(), 238.14285714285714)

    def test_max(self):
        self.assertEqual(task_1.maximum.max_of_elem(), 1563)

    def test_min(self):
        self.assertEqual(task_1.minimum.min_of_elem(), -101)


if __name__ == '__main__':
    unittest.main()
