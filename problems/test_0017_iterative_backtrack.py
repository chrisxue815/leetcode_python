import unittest


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digit_letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        zero = ord('0')
        digits = [ord(i) - zero for i in digits]
        n = len(digits)

        result = []
        indices = [0] * n
        result.append(''.join(digit_letters[digits[i]][0] for i in range(n)))

        while True:
            for i in range(n - 1, -1, -1):
                indices[i] += 1
                j = indices[i]
                if j < len(digit_letters[digits[i]]):
                    result.append(''.join(digit_letters[digits[i]][indices[i]] for i in range(n)))
                    break
                else:
                    indices[i] = 0
            else:
                return result


class Test(unittest.TestCase):
    def test(self):
        self._test("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
        self._test("", [])

    def _test(self, digits, expected):
        actual = Solution().letterCombinations(digits)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
