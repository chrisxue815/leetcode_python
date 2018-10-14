import unittest
import utils


# O(n) time. O(n) space. Math, hash table.
class Solution(object):
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
        cases = utils.load_json_from_path('../leetcode_test_cases/p888.json').test_cases

        for case in cases:
            actual = Solution().fairCandySwap(case.a, case.b)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
