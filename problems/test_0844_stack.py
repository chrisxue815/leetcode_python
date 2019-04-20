import unittest
import utils


def remove_backspace(s):
    result = []
    for ch in s:
        if ch == '#':
            if result:
                result.pop()
        else:
            result.append(ch)
    return result


# O(n) time. O(n) space. Stack.
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return remove_backspace(s) == remove_backspace(t)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().backspaceCompare(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
