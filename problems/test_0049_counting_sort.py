import collections
import unittest
from typing import List

import utils


def _count_sort(s):
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - ord('a')] += 1

    s = ''
    for i in range(26):
        s += chr(ord('a') + i) * counts[i]
    return s


# O(nm) time. O(nm) space. Anagram, counting sort, hash table.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for s in strs:
            anagrams[_count_sort(s)].append(s)

        return list(anagrams.values())


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().groupAnagrams(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
