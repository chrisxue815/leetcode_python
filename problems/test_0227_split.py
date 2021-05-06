import unittest

import utils


def multiply(s):
    result = 1
    multipliers = s.split('*')

    for multiplier in multipliers:
        if multiplier.startswith('/'):
            result = int(result / int(multiplier[1:]))
        else:
            result *= int(multiplier)

    return result


# O(n) time. O(n) space. Splitting.
class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        s = s.replace('-', '+-').replace('/', '*/')
        addends = s.split('+')

        for addend in addends:
            if '*' in addend:
                result += multiply(addend)
            else:
                result += int(addend)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
