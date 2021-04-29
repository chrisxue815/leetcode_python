import unittest
from typing import List

import utils


# O(n) time. O(1) space.
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = [0] * 26
        for c in chars:
            counts[ord(c) - ord('a')] += 1

        result = 0
        for word in words:
            remaining = counts.copy()
            for c in word:
                if remaining[ord(c) - ord('a')] <= 0:
                    break
                remaining[ord(c) - ord('a')] -= 1
            else:
                result += len(word)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().countCharacters(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
