import unittest


class Solution(object):
    def __init__(self):
        self.digit_letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.digits = None
        self.n = 0
        self.result = []

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        zero = ord('0')
        self.digits = [ord(i) - zero for i in digits]
        self.n = len(self.digits)

        self._backtrack(0, '')

        return self.result

    def _backtrack(self, start, s):
        if start == self.n:
            self.result.append(s)
        else:
            next_index = start + 1
            for ch in self.digit_letters[self.digits[start]]:
                self._backtrack(next_index, s + ch)


class Test(unittest.TestCase):
    def test(self):
        self._test("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self._test("", [])

    def _test(self, digits, expected):
        actual = Solution().letterCombinations(digits)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
