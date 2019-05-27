import unittest


class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        citations.sort(reverse=True)

        h = 0
        for i in citations:
            if i > h:
                h += 1
            else:
                break
        return h


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 0, 6, 1, 5], 3)
        self._test([2, 1], 1)

    def _test(self, citations, expected):
        actual = Solution().hIndex(citations)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
