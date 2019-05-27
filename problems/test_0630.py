import unittest
import heapq


# O(nlog(n)) time. O(n) space. Greedy.
class Solution:
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda it: it[1])

        time = 0
        q = []

        for t, d in courses:
            time += t
            if time <= d:
                heapq.heappush(q, -t)
            else:
                time += heapq.heappushpop(q, -t)

        return len(q)


class Test(unittest.TestCase):
    def test(self):
        self._test([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3)
        self._test([[1, 1]], 1)
        self._test([[1, 2], [2, 3]], 2)
        self._test([[10, 20], [4, 13], [4, 4], [3, 11], [3, 5], [3, 5]], 4)
        self._test([[9, 14], [7, 12], [1, 11], [4, 7]], 3)
        self._test([[9, 20], [4, 14], [4, 10], [6, 7], [2, 14], [8, 10], [6, 6], [5, 7]], 4)

    def _test(self, courses, expected):
        actual = Solution().scheduleCourse(courses)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
