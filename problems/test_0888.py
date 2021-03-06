import unittest
import utils


# O(n) time. O(n) space. Math, hash table.
class Solution:
    def fairCandySwap(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        sum_a = sum(a)
        sum_b = sum(b)
        avg = (sum_a + sum_b) / 2
        offset = avg - sum_b
        a = set(a)

        for size in b:
            if offset + size in a:
                return [offset + size, size]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().fairCandySwap(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
