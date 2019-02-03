import unittest


def binary_search(a, x, left=0, right=-1):
    """
    Returns the index of x if it exists in a.
    Otherwise returns the index of either its left or right neighbor.
    right is inclusive.
    """
    n = len(a)
    if right < 0:
        right += n

    while left < right:
        mid = left + (right - left) // 2
        if x < a[mid]:
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            return mid
    return left


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        if not nums1:
            return []

        # binary insertion sort nums1
        sorted_len = 1
        for i in range(1, len(nums1)):
            next_val = nums1[i]
            index = binary_search(nums1, next_val, 0, sorted_len - 1)
            if next_val < nums1[index]:
                nums1[index + 1: sorted_len + 1] = nums1[index: sorted_len]
                nums1[index] = next_val
                sorted_len += 1
            elif nums1[index] < next_val:
                nums1[index + 2: sorted_len + 1] = nums1[index + 1: sorted_len]
                nums1[index + 1] = next_val
                sorted_len += 1

        result = []
        for num in nums2:
            # binary search in nums1
            index_nums1 = binary_search(nums1, num, 0, sorted_len - 1)
            if nums1[index_nums1] != num:
                continue

            if not result:
                result.append(num)
            else:
                # binary search in result
                index_result = binary_search(result, num)
                if num < result[index_result]:
                    result[index_result + 1: len(result) + 1] = result[index_result: len(result)]
                    result[index_result] = num
                if result[index_result] < num:
                    if index_result + 1 < len(result):
                        result[index_result + 2: len(result) + 1] = result[index_result + 1: len(result)]
                        result[index_result + 1] = num
                    else:
                        result.append(num)

            if len(result) == len(nums1):
                break

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 1], [2, 2], [2])
        self._test([], [1], [])
        self._test([2, 1], [1, 2], [1, 2])

    def _test(self, nums1, nums2, result):
        actual = Solution().intersection(nums1, nums2)
        self.assertEqual(result, actual)


if __name__ == '__main__':
    unittest.main()
