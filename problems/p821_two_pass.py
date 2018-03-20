import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        distances = [0] * len(s)
        prev = -len(s)

        for i in xrange(len(s)):
            if s[i] == c:
                prev = i
            else:
                distances[i] = i - prev

        prev = len(s) << 1

        for i in xrange(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i
            else:
                distances[i] = min(distances[i], prev - i)

        return distances


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p821.json').test_cases

        for case in cases:
            actual = Solution().shortestToChar(case.s, case.c)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()