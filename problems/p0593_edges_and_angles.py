import unittest


def _edge(a, b):
    return b[0] - a[0], b[1] - a[1]


def _len_sq(a):
    return a[0] * a[0] + a[1] * a[1]


def _perpendicular(a, b):
    return not a[0] * a[1] + b[0] * b[1]


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])

        if p1[0] == p2[0] and p1[1] == p2[1]:
            return False

        if (p1[1] > p2[1]) != (p3[1] > p4[1]):
            p1, p2 = p2, p1

        e1 = _edge(p1, p2)
        e2 = _edge(p2, p4)
        e3 = _edge(p4, p3)
        e4 = _edge(p3, p1)

        edge = _len_sq(e1)
        return edge == _len_sq(e2) and edge == _len_sq(e3) and edge == _len_sq(e4) and _perpendicular(e1, e2)


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
