import unittest


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == '.':
                    continue

                num = ord(num) - ord('1')

                if rows[i][num]:
                    return False
                rows[i][num] = 1

                if cols[j][num]:
                    return False
                cols[j][num] = 1

                box_index = i // 3 * 3 + j // 3
                if boxes[box_index][num]:
                    return False
                boxes[box_index][num] = 1

        return True


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [
                ".87654321",
                "2........",
                "3........",
                "4........",
                "5........",
                "6........",
                "7........",
                "8........",
                "9........",
            ],
            True
        )

    def _test(self, board, expected):
        actual = Solution().isValidSudoku(board)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
