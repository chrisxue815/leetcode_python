import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution:
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        distances = [0] * len(s)
        prev = -len(s)

        for i in range(len(s)):
            if s[i] == c:
                prev = i
            else:
                distances[i] = i - prev

        prev = len(s) << 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i
            else:
                distances[i] = min(distances[i], prev - i)

        return distances


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().shortestToChar(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
