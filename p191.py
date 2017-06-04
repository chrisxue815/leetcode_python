import unittest


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Hacker's Delight, Figure 5-1
        n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f)
        n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff)
        n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)
        return n


class Test(unittest.TestCase):
    def test(self):
        self._test(11, 3)

    def _test(self, n, expected):
        actual = Solution().hammingWeight(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
