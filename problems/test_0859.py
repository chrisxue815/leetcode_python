import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def buddyStrings(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        if len(a) != len(b):
            return False

        diff1 = -1
        diff2 = -1

        for i in range(len(a)):
            if a[i] != b[i]:
                if diff1 == -1:
                    diff1 = i
                elif diff2 == -1 and a[diff1] == b[i] and a[i] == b[diff1]:
                    diff2 = i
                else:
                    return False

        if diff1 != -1:
            return diff2 != -1

        if len(a) > 26:
            return True

        count = [0] * 256
        for ch in a:
            if count[ord(ch)] >= 1:
                return True
            count[ord(ch)] += 1

        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().buddyStrings(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
