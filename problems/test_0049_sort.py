import itertools
import unittest
from typing import List

import utils


# O(n * mlog(m)). O(nm) space. Anagram, sorting.
# n = strs.length
# m = strs[i].length
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = sorted((sorted(s), s) for s in strs)
        groups = itertools.groupby(sorted_strs, key=lambda t: t[0])
        return [[t[1] for t in group] for _, group in groups]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, case, actual, msg):
        expected = sorted(sorted(group) for group in case.expected)
        actual = sorted(sorted(group) for group in actual)
        self.assertEqual(expected, actual, msg)


if __name__ == '__main__':
    unittest.main()
