import unittest


# O(n)
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = [0] * n
        lo = 1
        hi = n
        is_lo = True

        for i in xrange(k - 1):
            if is_lo:
                result[i] = lo
                lo += 1
            else:
                result[i] = hi
                hi -= 1
            is_lo ^= 1

        if is_lo:
            inc = 1
        else:
            inc = -1
            lo = hi

        for i in xrange(k - 1, n):
            result[i] = lo
            lo += inc

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(3, 1, [1, 2, 3])
        self._test(3, 2, [1, 3, 2])

    def _test(self, n, k, expected):
        actual = Solution().constructArray(n, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
