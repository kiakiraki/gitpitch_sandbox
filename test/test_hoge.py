import unittest
import hoge


class TestHoge(unittest.TestCase):
    def test_hoge(self):
        self.assertEqual(hoge.print_hoge(), 'hoge')

    def test_tashizan(self):
        self.assertEqual(hoge.tashizan(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
