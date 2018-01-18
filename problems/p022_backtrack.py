import unittest


class Solution(object):
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self._generate('', n, n, 0)
        return self.result

    def _generate(self, s, left, right, sum_):
        if left == 0:
            if right == 0:
                self.result.append(s)
            else:
                self.result.append(s + ')' * right)
        else:
            self._generate(s + '(', left - 1, right, sum_ + 1)
            if sum_ > 0:
                self._generate(s + ')', left, right - 1, sum_ - 1)


class Test(unittest.TestCase):
    def test(self):
        self._test(3, [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ])

    def _test(self, n, expected):
        actual = Solution().generateParenthesis(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
