import unittest
from main import currencyAMD
class TestCurrencyConverter(unittest.TestCase):
    def testroot(self):
        res = currencyAMD(1)
        self.assertEqual(res, '0.154125')

    def testnull(self):
        res = currencyAMD(-1)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
