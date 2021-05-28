import unittest
from typing import List

import utils

digit_letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


# O(4^n) time. O(4^n) space. Iterative backtracking.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
        digits = [ord(i) - ord('0') for i in digits]
        indices = [0] * len(digits)
        result.append(''.join(digit_letters[digit][0] for digit in digits))

        while True:
            for i in range(len(digits) - 1, -1, -1):
                indices[i] += 1
                j = indices[i]
                if j < len(digit_letters[digits[i]]):
                    result.append(''.join(digit_letters[digits[i]][indices[i]] for i in range(len(digits))))
                    break
                else:
                    indices[i] = 0
            else:
                return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, args, actual, msg):
        self.assertCountEqual(args.expected, actual, msg)


if __name__ == '__main__':
    unittest.main()
