import unittest


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return people

        people.sort(lambda x, y: y[0] - x[0] if x[0] != y[0] else x[1] - y[1])

        i = 1
        while i < len(people) and people[i][0] == people[0][0]:
            i += 1

        for i in xrange(i, len(people)):
            if people[i][1] < i:
                people.insert(people[i][1], people.pop(i))

        return people


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        )

    def _test(self, people, expected):
        actual = Solution().reconstructQueue(people)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
