import unittest

from typing import List

import utils


# O(len(nums1) * len(nums2)) time. O(1) space. Monotone stack, hash table.
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for num in nums1:
            index = nums2.index(num)
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    result.append(nums2[i])
                    break
            else:
                result.append(-1)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().nextGreaterElement(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
