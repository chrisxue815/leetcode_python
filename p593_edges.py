import unittest


def _edge_len_sq(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    return x * x + y * y


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        edges = {
            _edge_len_sq(p1, p2),
            _edge_len_sq(p1, p3),
            _edge_len_sq(p1, p4),
            _edge_len_sq(p2, p3),
            _edge_len_sq(p2, p4),
            _edge_len_sq(p3, p4),
        }

        return len(edges) == 2 and 0 not in edges


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 0], [0, 1], [1, 1], [1, 0], True)
        self._test([0, 0], [0, 1], [1, 0], [1, 1], True)
        self._test([0, 0], [1, 1], [0, 1], [1, 0], True)
        self._test([0, 0], [1, 1], [1, 0], [0, 1], True)
        self._test([0, 0], [0, 2], [-1, 1], [1, 1], True)
        self._test([0, 0], [0, 0], [0, 0], [0, 0], False)
        self._test([0, 0], [0, 0], [0, 0], [1, 1], False)

    def _test(self, p1, p2, p3, p4, expected):
        actual = Solution().validSquare(p1, p2, p3, p4)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
