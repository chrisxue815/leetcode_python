import unittest


class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) < 4:
            return False

        inward = False
        right = prev_left = 0
        bot = prev_top = 0
        top = prev_bot = x[0]
        left = prev_right = -x[1]

        for i in xrange(2, len(x)):
            direction = i & 3
            if direction == 2:
                new_bot = top - x[i]
                if inward:
                    if new_bot <= bot:
                        return True
                elif new_bot >= bot:
                    inward = True
                    if new_bot <= prev_top:
                        right = prev_left
                prev_bot, bot = bot, new_bot
            elif direction == 3:
                new_right = left + x[i]
                if inward:
                    if new_right >= right:
                        return True
                elif new_right <= right:
                    inward = True
                    if new_right >= prev_left:
                        top = prev_bot
                prev_right, right = right, new_right
            elif direction == 0:
                new_top = bot + x[i]
                if inward:
                    if new_top >= top:
                        return True
                elif new_top <= top:
                    inward = True
                    if new_top >= prev_bot:
                        left = prev_right
                prev_top, top = top, new_top
            elif direction == 1:
                new_left = right - x[i]
                if inward:
                    if new_left <= left:
                        return True
                elif new_left >= left:
                    inward = True
                    if new_left <= prev_right:
                        bot = prev_top
                prev_left, left = left, new_left

        return False


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 1, 1, 2], True)

        self._test([1, 2, 3, 4], False)

        self._test([1, 1, 1, 1], True)

        self._test([1, 2, 3, 8, 2, 2, 1], False)
        self._test([1, 2, 3, 8, 2, 2, 2], True)
        self._test([1, 2, 3, 8, 2, 2, 3], True)

        self._test([3, 3, 4, 2, 2], False)

    def _test(self, x, expected):
        actual = Solution().isSelfCrossing(x)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
