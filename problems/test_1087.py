import itertools
import re
import unittest
from typing import List

import utils


# O(n + len(options) * len(groups)) time. O(n) space. String.
class Solution:
    def expand(self, S: str) -> List[str]:
        groups = re.split(r'[{}]', S)
        groups = (sorted(options.split(',')) for options in groups)
        return [''.join(options) for options in itertools.product(*groups)]

    def expand_one_liner(self, S: str) -> List[str]:
        return [''.join(options) for options in itertools.product(*(sorted(options.split(',')) for options in re.split(r'[{}]', S)))]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().expand(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
