import unittest

import utils


# O(n) time. O(1) space. Bit manipulation.
class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        result = [False] * len(A)
        num = 0

        for i, bit in enumerate(A):
            num = (num << 1) | bit
            result[i] = num % 5 == 0

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().prefixesDivBy5(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()