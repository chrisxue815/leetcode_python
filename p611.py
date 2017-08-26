import unittest


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0

        for i in xrange(0, len(nums) - 2):
            if nums[i] == 0:
                continue

            a = nums[i]
            k = i + 2
            for j in xrange(i + 1, len(nums) - 1):
                b = nums[j]
                while k < len(nums) and a + b > nums[k]:
                    k += 1
                result += k - j - 1

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 2, 3, 4], 3)

    def _test(self, n, expected):
        actual = Solution().triangleNumber(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
