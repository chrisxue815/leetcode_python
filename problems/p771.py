import unittest
import utils


# O(n) time. O(n) space. Hash table.
class Solution(object):
    def numJewelsInStones(self, j, s):
        """
        :type j: str
        :type s: str
        :rtype: int
        """
        j = set(j)
        return sum(stone in j for stone in s)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p771.json').test_cases

        for case in cases:
            actual = Solution().numJewelsInStones(case.j, case.s)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
