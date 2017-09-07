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
            for i, ch in enumerate(senate):
                if ch == 'R':
                    d -= 1
                    if d <= 0:
                        return 'Radiant'
                    ch = 'D'
                elif ch == 'D':
                    r -= 1
                    if r <= 0:
                        return 'Dire'
                    ch = 'R'
                else:
                    continue

                for j in xrange(i + 1, len(senate)):
                    if senate[j] == ch:
                        senate[j] = 0
                        break

            senate = filter(lambda a: a != 0, senate)


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
