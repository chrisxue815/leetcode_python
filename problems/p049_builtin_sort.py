import collections
import unittest


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = collections.defaultdict(list)

        for s in strs:
            anagrams[''.join((sorted(s)))].append(s)

        return anagrams.values()


class Test(unittest.TestCase):
    def test(self):
        self._test(["eat", "tea", "tan", "ate", "nat", "bat"], [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ])

    def _test(self, strs, expected):
        actual = Solution().groupAnagrams(strs)
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
