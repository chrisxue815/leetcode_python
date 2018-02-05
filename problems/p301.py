import unittest


def _dfs_left_to_right(s, start, last_deleted, results):
    counter = 0
    for i in xrange(start, len(s)):
        if s[i] == '(':
            counter += 1
        elif s[i] == ')':
            counter -= 1
            if counter < 0:
                for j in xrange(last_deleted, i + 1):
                    if s[j] == ')' and (j == last_deleted or s[j - 1] != ')'):
                        _dfs_left_to_right(s[:j] + s[j + 1:], i, j, results)
                return

    _dfs_right_to_left(s, len(s) - 1, len(s) - 1, results)


def _dfs_right_to_left(s, start, last_deleted, results):
    counter = 0
    for i in xrange(start, -1, -1):
        if s[i] == ')':
            counter -= 1
        elif s[i] == '(':
            counter += 1
            if counter > 0:
                for j in xrange(last_deleted, i - 1, -1):
                    if s[j] == '(' and (j == last_deleted or s[j + 1] != '('):
                        _dfs_right_to_left(s[:j] + s[j + 1:], i - 1, j - 1, results)
                return

    results.append(s)


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        _dfs_left_to_right(s, 0, 0, result)
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test('()())()', ['()()()', '(())()'])
        self._test('(a)())()', ['(a)()()', '(a())()'])
        self._test(')(', [''])
        self._test('(', [''])
        self._test('((', [''])
        self._test(')', [''])
        self._test('))', [''])
        self._test('())', ['()'])
        self._test('()))', ['()'])
        self._test('(()', ['()'])
        self._test('((()', ['()'])
        self._test('(r(()()(', ["r()()", "r(())", "(r)()", "(r())"])

    def _test(self, s, expected):
        actual = Solution().removeInvalidParentheses(s)
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()