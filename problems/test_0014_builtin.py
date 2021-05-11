import os
import unittest
from typing import List

import utils


# O(n) time. O(1) space. Built-in method.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)
