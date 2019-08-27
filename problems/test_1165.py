import unittest

import utils


# O(n) time. O(1) space. Hash table.
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        result = 0
        curr = 0
        char_to_index = {c: i for i, c in enumerate(keyboard)}

        for c in word:
            i = char_to_index[c]
            result += abs(i - curr)
            curr = i

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().calculateTime(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
