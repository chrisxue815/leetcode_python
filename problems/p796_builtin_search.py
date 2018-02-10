import unittest
import utils


# Built-in string searching.
class Solution(object):
    def rotateString(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        if len(a) != len(b):
            return False

        a += a

        # CPython fast search
        # https://github.com/python/cpython/blob/master/Objects/stringlib/fastsearch.h
        return b in a


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p796.json').test_cases

        for case in cases:
            actual = Solution().rotateString(case.a, case.b)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
