import unittest


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        visited = [0] * (len(nums) + 1)

        for num in nums:
            visited[num] = 1

        result = []
        for i in xrange(1, len(visited)):
            if visited[i] == 0:
                result.append(i)

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 3, 2, 7, 8, 2, 3, 1], [5, 6])

    def _test(self, nums, expected):
        actual = Solution().findDisappearedNumbers(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
