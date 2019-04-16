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

        # See CPython fast search
        # https://github.com/python/cpython/blob/master/Objects/stringlib/fastsearch.h
        return b in a


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().rotateString(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
