import unittest
from typing import List

import utils


# O(n) time. O(1) space. Iteration.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]

        for i, c in enumerate(a):
            for j in range(1, len(strs)):
                b = strs[j]
                if i >= len(b) or b[i] != c:
                    return a[:i]

        return a


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)
