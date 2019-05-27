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
        result = ['']

        for digit_ch in digits:
            digit = ord(digit_ch) - zero
            new_result = []
            for combination in result:
                for letter in digit_letters[digit]:
                    new_result.append(combination + letter)
            result = new_result
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
