import unittest
from typing import List

import utils

digit_letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


# O(4^n) time. O(4^n) space. Cartesian product.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = ['']

        for digit_ch in digits:
            digit = ord(digit_ch) - ord('0')
            new_result = []
            for combination in result:
                for letter in digit_letters[digit]:
                    new_result.append(combination + letter)
            result = new_result
        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, asserter=self.assertCountEqual)


if __name__ == '__main__':
    unittest.main()
