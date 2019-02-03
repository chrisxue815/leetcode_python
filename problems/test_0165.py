import unittest


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = [int(s) for s in version1.split('.')]
        version2 = [int(s) for s in version2.split('.')]

        for v1, v2 in zip(version1, version2):
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        if len(version1) < len(version2):
            return 0 if all(v == 0 for v in version2[len(version1):]) else -1
        elif len(version1) > len(version2):
            return 0 if all(v == 0 for v in version1[len(version2):]) else 1
        return 0


class Test(unittest.TestCase):
    def test(self):
        self._test('0.1.345', '0.1.346', -1)
        self._test('0.1', '1.1', -1)
        self._test('0.1', '0.1', 0)
        self._test('0.1', '0.1.1', -1)
        self._test('0.1', '0.1.0', 0)

    def _test(self, version1, version2, expected):
        actual = Solution().compareVersion(version1, version2)
        self.assertEqual(expected, actual)

        actual = Solution().compareVersion(version2, version1)
        self.assertEqual(-expected, actual)


if __name__ == '__main__':
    unittest.main()
