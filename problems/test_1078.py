import unittest
from typing import List

import utils


# O(n) time. O(n) space. String.
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        return [words[i + 2] for i in range(len(words) - 2) if words[i] == first and words[i + 1] == second]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().findOcurrences(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
