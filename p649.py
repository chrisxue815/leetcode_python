import unittest


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r = senate.count('R')
        d = len(senate) - r

        senate = list(senate)

        while True:
            i = 0
            while i < len(senate):
                if senate[i] == 'R':
                    d -= 1
                    if d <= 0:
                        return 'Radiant'
                    ch = 'D'
                else:
                    r -= 1
                    if r <= 0:
                        return 'Dire'
                    ch = 'R'

                for j in xrange(i + 1, len(senate)):
                    if senate[j] == ch:
                        senate.pop(j)
                        break

                i += 1


class Test(unittest.TestCase):
    def test(self):
        self._test('RD', 'Radiant')
        self._test('RDD', 'Dire')
        self._test('DRRD', 'Dire')
        self._test('DRRDRDRDRDDRDRDR', 'Radiant')

    def _test(self, senate, expected):
        actual = Solution().predictPartyVictory(senate)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
