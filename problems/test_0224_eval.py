import unittest

import utils


# Built-in eval function
class Solution:
    def calculate(self, s: str) -> int:
        return eval(s)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
