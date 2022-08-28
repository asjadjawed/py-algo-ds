import unittest
from src.recursion.fib import fib_rec, fib_rec_memo, fib_iter


class TestFib(unittest.TestCase):

    def test_zero(self):
        '''Fib of 0'''
        self.assertEqual(fib_rec(0), 0)
        self.assertEqual(fib_rec_memo(0), 0)
        self.assertEqual(fib_iter(0), 0)

    def test_one(self):
        '''Fib of 1'''
        self.assertEqual(fib_rec(1), 1)
        self.assertEqual(fib_rec_memo(1), 1)
        self.assertEqual(fib_iter(1), 1)

    def test_two(self):
        '''Fib of 2'''
        self.assertEqual(fib_rec(2), 1)
        self.assertEqual(fib_rec_memo(2), 1)
        self.assertEqual(fib_iter(2), 1)

    def test_five(self):
        '''Fib of 5'''
        self.assertEqual(fib_rec(5), 5)
        self.assertEqual(fib_rec_memo(5), 5)
        self.assertEqual(fib_iter(5), 5)

    def test_ten(self):
        '''Fib of 10'''
        self.assertEqual(fib_rec(10), 55)
        self.assertEqual(fib_rec_memo(10), 55)
        self.assertEqual(fib_iter(10), 55)


if __name__ == "__main__":
    unittest.main()
