import unittest
import utils


# O(n) time. O(n) space. Hash table.
class Solution(object):
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
        cases = utils.load_json_from_path('../leetcode_test_cases/p961.json').test_cases

        for case in cases:
            actual = Solution().repeatedNTimes(case.a)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
