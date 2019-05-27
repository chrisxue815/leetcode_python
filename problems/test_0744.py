import unittest


# O(log(n)) time. O(1) space. Binary search.
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        lo = 0
        hi = len(letters) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            mid_val = letters[mid]
            if mid_val <= target:
                lo = mid + 1
            else:
                hi = mid - 1

        return letters[lo] if lo < len(letters) else letters[0]


class Test(unittest.TestCase):
    def test(self):
        test_cases = [
            [["c", "f", "j"], "a", "c"],
            [["c", "f", "j"], "c", "f"],
            [["c", "f", "j"], "d", "f"],
            [["c", "f", "j"], "g", "j"],
            [["c", "f", "j"], "j", "c"],
            [["c", "f", "j"], "k", "c"],
        ]

        for test_case in test_cases:
            actual = Solution().nextGreatestLetter(*test_case[:-1])
            self.assertEqual(test_case[-1], actual)


if __name__ == '__main__':
    unittest.main()
