import unittest
import collections

max_balls = 6


def _delete_3balls(board, lo, hi):
    if lo < 0:
        return board[:lo + 1] + board[hi:]
    while True:
        ball = board[lo]
        new_lo, new_hi = lo - 1, hi
        while new_lo >= 0 and board[new_lo] == ball:
            new_lo -= 1
        while new_hi < len(board) and board[new_hi] == ball:
            new_hi += 1
        if lo - new_lo + new_hi - hi >= 3:
            lo, hi = new_lo, new_hi
        else:
            break
    return board[:lo + 1] + board[hi:]


def _dfs(board, hand, inserted, num_inserted, min_num_inserted):
    if not board:
        return num_inserted
    if num_inserted >= min_num_inserted:
        return min_num_inserted

    for ball, num_balls in hand.iteritems():
        if inserted[ball] >= num_balls:
            continue

        for i in xrange(len(board)):
            if board[i] != ball:
                continue
            if i + 1 < len(board) and board[i] == board[i + 1]:
                new_board = _delete_3balls(board, i - 1, i + 2)
                inserted[ball] += 1
                min_num_inserted = _dfs(new_board, hand, inserted, num_inserted + 1, min_num_inserted)
                inserted[ball] -= 1
            elif inserted[ball] + 2 <= num_balls:
                new_board = _delete_3balls(board, i - 1, i + 1)
                inserted[ball] += 2
                min_num_inserted = _dfs(new_board, hand, inserted, num_inserted + 2, min_num_inserted)
                inserted[ball] -= 2

    return min_num_inserted


class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        hand = collections.Counter(hand)
        inserted = collections.Counter()
        min_inserted_balls = _dfs(board, hand, inserted, 0, max_balls)

        return min_inserted_balls if min_inserted_balls < max_balls else -1


class Test(unittest.TestCase):
    def test(self):
        self._test('WRRBBW', 'RB', -1)
        self._test('WWRRBBWW', 'WRBRW', 2)
        self._test('G', 'GGGGG', 2)
        self._test('RBYYBBRRB', 'YRBGB', 3)

    def _test(self, board, hand, expected):
        actual = Solution().findMinStep(board, hand)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
