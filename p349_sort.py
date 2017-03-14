import unittest


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()

        result = []
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if not result or nums1[i] != result[-1]:
                    result.append(nums1[i])
                i += 1
                j += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 1], [2, 2], [2])
        self._test([], [1], [])
        self._test([2, 1], [1, 2], [1, 2])

    def _test(self, nums1, nums2, result):
        actual = Solution().intersection(nums1, nums2)
        self.assertEqual(actual, result)


if __name__ == '__main__':
    unittest.main()
