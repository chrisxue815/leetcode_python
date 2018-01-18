import unittest


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lr = ud = 0
        for move in moves:
            if move == 'L':
                lr += 1
            elif move == 'R':
                lr -= 1
            elif move == 'U':
                ud += 1
            else:
                ud -= 1
        return lr == 0 and ud == 0


class Test(unittest.TestCase):
    def test(self):
        self._test('UD', True)
        self._test('LL', False)

    def _test(self, moves, expected):
        actual = Solution().judgeCircle(moves)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
