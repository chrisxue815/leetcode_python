import unittest


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for ch in s:
            # is "if" faster or slower than hash table in python?
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif ch == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif ch == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        return not stack


class Test(unittest.TestCase):
    def test(self):
        self._test('()', True)
        self._test('()[]{}', True)
        self._test('(]', False)
        self._test('([)]', False)
        self._test(')', False)

    def _test(self, n, expected):
        actual = Solution().isValid(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
