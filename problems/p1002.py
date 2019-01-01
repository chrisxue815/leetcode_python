import collections
import functools
import unittest
import utils


# O(n) time. O(1) space. Hash table.
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        a = collections.Counter(A[0])
        strings = iter(A)
        next(strings)

        for s in strings:
            b = collections.Counter(s)
            a = {ch: min(count, b[ch]) for ch, count in a.iteritems()}

        return functools.reduce(lambda accum, (ch, count): accum + [ch] * count, a.iteritems(), [])


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().commonChars(case.A)
            self.assertItemsEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
