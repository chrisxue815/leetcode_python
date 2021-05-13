import collections
import unittest
from typing import List

import utils


# O(n * mlog(m)). O(nm) space. Anagram, hash table, sorting.
# n = strs.length
# m = strs[i].length
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)

        for s in strs:
            result[''.join(sorted(s))].append(s)

        return list(result.values())


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, expected, actual, msg, case):
        expected = sorted(sorted(group) for group in expected)
        actual = sorted(sorted(group) for group in actual)
        self.assertEqual(expected, actual, msg)


if __name__ == '__main__':
    unittest.main()
