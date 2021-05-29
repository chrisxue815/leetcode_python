import unittest
from typing import List

import utils

digit_letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


# O(4^n) time. O(4^n) space. Recursive backtracking.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
        digits = [ord(i) - ord('0') for i in digits]

        def dfs(cur, s):
            if cur == len(digits):
                result.append(s)
            else:
                nxt = cur + 1
                for ch in digit_letters[digits[cur]]:
                    dfs(nxt, s + ch)

        dfs(0, '')

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, asserter=self.assertCountEqual)


if __name__ == '__main__':
    unittest.main()
