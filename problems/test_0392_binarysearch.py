import unittest

import utils


def _binary_search(a, x, lo, hi):
    while lo <= hi:
        mid = lo + ((hi - lo) >> 1)
        mid_val = a[mid]
        if mid_val < x:
            lo = mid + 1
        elif mid_val > x:
            hi = mid - 1
        else:
            return mid

    return lo


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        base = ord('a')
        index_map = [[] for i in range(26)]
        for i in range(len(t)):
            index_map[ord(t[i]) - base].append(i)

        index = 0
        for ch in s:
            indices = index_map[ord(ch) - base]
            i = _binary_search(indices, index, 0, len(indices) - 1)
            if i >= len(indices):
                return False
            index = indices[i] + 1

        return True


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
