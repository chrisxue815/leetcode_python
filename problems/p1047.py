import unittest

import utils


# O(n) time. O(n) space. String.
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 1

        while i < len(S):
            if S[i - 1] == S[i]:
                S = S[:i - 1] + S[i + 1:]
                if i > 1:
                    i -= 1
            else:
                i += 1

        return S


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().removeDuplicates(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
