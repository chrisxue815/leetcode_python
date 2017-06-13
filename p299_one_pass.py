import unittest


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cs = [0] * (ord('9') + 1)
        cg = [0] * (ord('9') + 1)
        for ds, dg in zip(secret, guess):
            ds, dg = ord(ds), ord(dg)
            if ds == dg:
                bulls += 1
            else:
                cs[ds] += 1
                cg[dg] += 1
        cows = sum(min(s, g) for s, g in zip(cs[ord('0'):], cg[ord('0'):]))
        return str(bulls) + 'A' + str(cows) + 'B'


class Test(unittest.TestCase):
    def test(self):
        self._test('1807', '7810', '1A3B')
        self._test('1123', '0111', '1A1B')
        self._test('1122', '1222', '3A0B')

    def _test(self, secret, guess, expected):
        actual = Solution().getHint(secret, guess)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
