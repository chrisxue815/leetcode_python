import unittest


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        visited = [0] * len(nums)

        for num in nums:
            visited[num - 1] = 1

        result = []
        for i in xrange(len(visited)):
            if visited[i] == 0:
                result.append(i + 1)

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 3, 2, 7, 8, 2, 3, 1], [5, 6])

    def _test(self, nums, expected):
        actual = Solution().findDisappearedNumbers(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
