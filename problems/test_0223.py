import unittest


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area = (C - A) * (D - B) + (G - E) * (H - F)
        if G <= A or C <= E or D <= F or H <= B:
            return area
        
        width = min(C, G) - max(A, E)
        height = min(D, H) - max(B, F)

        return area - width * height


class Test(unittest.TestCase):
    def test(self):
        self._test(-3, 0, 3, 4, 0, -1, 9, 2, 45)
        self._test(0, 0, 1, 1, 0, 0, 1, 1, 1)
        self._test(0, 0, 0, 0, -1, -1, 1, 1, 4)

    def _test(self, A, B, C, D, E, F, G, H, expected):
        actual = Solution().computeArea(A, B, C, D, E, F, G, H)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
