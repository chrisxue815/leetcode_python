import unittest


def is_subseq(a, b):
    i = 0
    for ch in b:
        if ch == a[i]:
            i += 1
            if i == len(a):
                return True
    return False


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(key=len, reverse=True)

        for i, a in enumerate(strs):
            for j, b in enumerate(strs):
                if i == j:
                    continue
                if len(b) < len(a):
                    return len(a)
                if is_subseq(a, b):
                    break
            else:
                return len(a)

        return -1


class Test(unittest.TestCase):
    def test(self):
        self._test(['aba', 'cdc'], 3)
        self._test(['abcd', 'abc'], 4)
        self._test(['abc', 'dbc'], 3)
        self._test(['abc', 'abc'], -1)
        self._test(['aba', 'cdc', 'eae'], 3)

    def _test(self, strs, expected):
        actual = Solution().findLUSlength(strs)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
