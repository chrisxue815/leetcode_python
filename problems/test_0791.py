import unittest
import utils


# O(n) time. O(1) space. Array.
class Solution:
    def customSortString(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counts = [0] * 128

        for ch in t:
            counts[ord(ch)] += 1

        result = ''

        for ch in s:
            result += ch * counts[ord(ch)]
            counts[ord(ch)] = 0

        for ch in range(ord('a'), ord('z') + 1):
            result += chr(ch) * counts[ch]

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().customSortString(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
