import collections
import unittest

_a = ord('a')


def _count_sort(s):
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - _a] += 1

    s = ''
    for i in range(26):
        s += chr(i + _a) * counts[i]
    return s


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = collections.defaultdict(list)

        for s in strs:
            anagrams[_count_sort(s)].append(s)

        return list(anagrams.values())


class Test(unittest.TestCase):
    def test(self):
        self._test(["eat", "tea", "tan", "ate", "nat", "bat"], [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ])

    def _test(self, strs, expected):
        actual = Solution().groupAnagrams(strs)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
