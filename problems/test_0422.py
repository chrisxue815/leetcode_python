import unittest
from typing import List

import utils


# O(n) time. O(n) space. Matrix.
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for r in range(len(words)):
            for c in range(r + 1, len(words[r])):
                if words[r][c] != words[c][r]:
                    return False

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().validWordSquare(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
