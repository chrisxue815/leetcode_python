import unittest
import utils


# O(n^2) time. O(1) space. Naive string searching.
class Solution(object):
    def rotateString(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        if len(a) != len(b):
            return False
        if not a:
            return True

        for start in range(len(a)):
            i = start - len(a)
            for j in range(len(a)):
                if a[i] != b[j]:
                    break
                i += 1
            else:
                return True

        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().rotateString(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
