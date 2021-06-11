import unittest

import utils


class ProductOfNumbers:

    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.products):
            return 0
        return self.products[-1] // self.products[-k - 1]


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, ProductOfNumbers)


if __name__ == '__main__':
    unittest.main()
