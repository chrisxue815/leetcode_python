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
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().diStringMatch(**case.args._asdict())
            self.assertCountEqual(list(range(len(case.args.s) + 1)), actual, msg=case.args)

            for i in range(len(case.args.s)):
                if case.args.s[i] == 'I':
                    self.assertLess(actual[i], actual[i + 1], msg=case.args)
                else:
                    self.assertGreater(actual[i], actual[i + 1], msg=case.args)


if __name__ == '__main__':
    unittest.main()
