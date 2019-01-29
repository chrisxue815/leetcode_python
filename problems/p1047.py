import unittest

import utils


# O(n) time. O(n) space. Stack.
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []

        for ch in S:
            stack.append(ch)

            while len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()

        return ''.join(stack)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().removeDuplicates(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
