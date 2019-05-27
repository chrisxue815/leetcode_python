import unittest
import utils


# O(n) time. O(1) space. Bit manipulation.
class Solution:
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        count = 1

        while n > 0 and n & 1 == 0:
            n >>= 1

        n >>= 1

        while n > 0:
            if n & 1 == 0:
                count += 1
            else:
                result = max(result, count)
                count = 1
            n >>= 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().binaryGap(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
