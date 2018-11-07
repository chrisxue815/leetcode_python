import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        lo = 0
        hi = len(s)
        result = []

        for ch in s:
            if ch == 'I':
                result.append(lo)
                lo += 1
            else:
                result.append(hi)
                hi -= 1

        result.append(lo)
        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p942.json').test_cases

        for case in cases:
            actual = Solution().diStringMatch(case.s)
            self.assertItemsEqual(range(len(case.s) + 1), actual)

            for i in xrange(len(case.s)):
                if case.s[i] == 'I':
                    self.assertLess(actual[i], actual[i + 1])
                else:
                    self.assertGreater(actual[i], actual[i + 1])


if __name__ == '__main__':
    unittest.main()
