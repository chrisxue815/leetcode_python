import unittest

import utils

rotate_to_other = [False, False, True, False, False, True, True, False, False, True]
invalid = [False, False, False, True, True, False, False, True, False, False]


def is_good(num):
    valid = False
    while num:
        num, r = divmod(num, 10)
        if invalid[r]:
            return False
        if rotate_to_other[r]:
            valid = True
    return valid


# O(n) time. O(1) space. Math.
class Solution:
    def rotatedDigits(self, n: int) -> int:
        return sum(is_good(num) for num in range(1, n + 1))


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
