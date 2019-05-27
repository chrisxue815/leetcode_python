import unittest
import re


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = re.match(
            '\A\s*[+-]?(?P<n1>[0-9]*)(\.(?P<n2>[0-9]*))?(?P<e>e\s*[+-]?(?P<n3>[0-9]*))?\s*\Z', s)
        if match is not None \
                and (match.group('n1') or match.group('n2')) \
                and (not match.group('e') or match.group('n3')):
            return True
        return False


class Test(unittest.TestCase):
    def test(self):
        self._test('0', True)
        self._test(' 0.1 ', True)
        self._test('abc', False)
        self._test('1 a', False)
        self._test('2e10', True)
        self._test(' 9 9 ', False)
        self._test('-1', True)
        self._test('+1', True)
        self._test(' +1.2e-1.2 ', False)
        self._test(' +1.2e-2 ', True)
        self._test(' +.2e-.2 ', False)
        self._test(' +.2e-2 ', True)
        self._test(' +1.e-1. ', False)
        self._test(' +1.e-2 ', True)
        self._test(' +.e-1 ', False)
        self._test(' e ', False)

    def _test(self, s, expected):
        actual = Solution().isNumber(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
