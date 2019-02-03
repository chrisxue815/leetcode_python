import unittest
import collections


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        r = collections.deque()
        d = collections.deque()

        for i, ch in enumerate(senate):
            if ch == 'R':
                r.append(i)
            else:
                d.append(i)

        while r and d:
            rl = r.popleft()
            dl = d.popleft()
            if rl < dl:
                r.append(rl + len(senate))
            else:
                d.append(dl + len(senate))

        return 'Radiant' if r else 'Dire'


class Test(unittest.TestCase):
    def test(self):
        self._test('RD', 'Radiant')
        self._test('RDD', 'Dire')
        self._test('DRRD', 'Dire')
        self._test('DRRDRDRDRDDRDRDR', 'Radiant')

    def _test(self, senate, expected):
        actual = Solution().predictPartyVictory(senate)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
