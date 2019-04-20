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
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().removeDuplicates(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
