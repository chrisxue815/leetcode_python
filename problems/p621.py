import unittest


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
        counts.sort(reverse=True)

        most_common = counts[0]
        for i, count in enumerate(counts):
            if count != most_common:
                break
        else:
            i = 26

        return max(len(tasks), (counts[0] - 1) * (n + 1) + i)


class Test(unittest.TestCase):
    def test(self):
        self._test(['A', 'A', 'A', 'B', 'B', 'B'], 2, 8)
        self._test(['A', 'A', 'B', 'C', 'D', 'E'], 1, 6)
        self._test(['A', 'A', 'B', 'B', 'C', 'C'], 1, 6)
        self._test(['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'], 1, 8)
        self._test([chr(i + ord('A')) for i in xrange(26)] * 2, 26, 53)

    def _test(self, tasks, n, expected):
        actual = Solution().leastInterval(tasks, n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
