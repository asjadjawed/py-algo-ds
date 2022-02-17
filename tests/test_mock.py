import unittest
from src.utils.mock import mock


class TestMock(unittest.TestCase):
    def setUp(self):
        print('running tests...')

    def test_mock(self):
        '''A mock function'''
        self.assertEqual(mock(), "Hello Python!")

    def tearDown(self):
        print('done testing')


if __name__ == "__main__":
    unittest.main()
