import unittest
import utils


# O(n) time. O(n) space. Hash table.
class Solution:
    def repeatedNTimes(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        visited = set()

        for num in a:
            if num in visited:
                return num
            visited.add(num)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().repeatedNTimes(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
