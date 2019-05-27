import unittest


def _binary_search(a, x, lo=0, hi=-1):
    if hi < 0:
        hi += len(a)

    while lo <= hi:
        mid = lo + ((hi - lo) >> 1)
        mid_val = a[mid]
        if mid_val < x:
            lo = mid + 1
        elif mid_val > x:
            hi = mid - 1
        else:
            return mid

    return ~lo


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        D.sort()

        for a in A:
            for b in B:
                for c in C:
                    target = -a - b - c
                    d_index = _binary_search(D, target)
                    if d_index >= 0:
                        d = D[d_index]
                        i = d_index
                        while i >= 0 and D[i] == d:
                            count += 1
                            i -= 1
                        i = d_index + 1
                        while i < len(D) and D[i] == d:
                            count += 1
                            i += 1

        return count


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2], [-2, -1], [-1, 2], [0, 2], 2)
        self._test([1, 2], [-2, -1], [-1, -1, 2], [0, 2, 2], 6)

    def _test(self, a, b, c, d, expected):
        actual = Solution().fourSumCount(a, b, c, d)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
