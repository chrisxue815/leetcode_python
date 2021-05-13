import collections
import unittest
from typing import List

import utils


def get_key(s):
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - ord('a')] += 1
    return tuple(counts)


# O(nm) time. O(n) space. Anagram, hash table, counting.
# n = strs.length
# m = strs[i].length
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)

        for s in strs:
            result[get_key(s)].append(s)

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
