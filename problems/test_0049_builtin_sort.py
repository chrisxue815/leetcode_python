import collections
import unittest
from typing import List

import utils


# O(n * mlog(m)). O(nm) space. Anagram, sorting, hash table.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for s in strs:
            anagrams[''.join(sorted(s))].append(s)

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
