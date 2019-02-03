import unittest


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda h_k: (-h_k[0], h_k[1]))

        r = []
        for p in people:
            r.insert(p[1], p)

        return r


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        )

    def _test(self, people, expected):
        actual = Solution().reconstructQueue(people)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
