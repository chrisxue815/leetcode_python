import functools
import unittest


def _compare(a, b):
    if len(a) < len(b):
        return 1
    elif len(a) > len(b):
        return -1
    else:
        for x, y in zip(a, b):
            if x < y:
                return -1
            elif x > y:
                return 1
        return 0


class Solution(object):
    def findLongestWord(self, a, d):
        """
        :type a: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=functools.cmp_to_key(_compare))
        for b in d:
            if len(a) < len(b):
                continue
            na = len(a)
            nb = len(b)
            i = 0
            j = 0
            while na - i >= nb - j and j < nb:
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == nb:
                return b
        return ''


class Test(unittest.TestCase):
    def test(self):
        self._test('abpcplea', ['ale', 'apple', 'monkey', 'plea'], 'apple')
        self._test('abpcplea', ['a', 'b', 'c'], 'a')
        self._test('d', ['a', 'b', 'c'], '')

    def _test(self, s, d, expected):
        actual = Solution().findLongestWord(s, d)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
