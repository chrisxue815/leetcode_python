import functools
import unittest
from typing import List

import utils


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        @functools.lru_cache(None)
        def suffix(w1, w2):
            best = w2
            for i in range(len(w1) + 1):
                if w2.startswith(w1[-i:]):
                    best = w2[i:]
            return best

        @functools.lru_cache(None)
        def dp(state, last):
            if state + 1 == 1 << n:
                return ''
            return min(
                [suffix(words[last], words[i]) + dp(state | (1 << i), i) for i in range(n) if state & (1 << i) == 0],
                key=len)

        n = len(words)
        return min([words[i] + dp(1 << i, i) for i in range(n)], key=len)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, case, actual, msg):
        self.assertEqual(len(case.expected), len(actual), msg)


if __name__ == '__main__':
    unittest.main()
