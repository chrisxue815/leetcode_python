import itertools
import unittest
from typing import List

import utils


# O(n + len(options) * len(groups)) time. O(n) space. String.
class Solution:
    def expand(self, S: str) -> List[str]:
        groups = []
        options = []
        in_braces = False

        for c in S:
            if c == '{':
                in_braces = True
            elif c == '}':
                options.sort()
                groups.append(options)
                options = []
                in_braces = False
            elif c == ',':
                pass
            else:
                if in_braces:
                    options.append(c)
                else:
                    groups.append([c])

        return [''.join(options) for options in itertools.product(*groups)]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().expand(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
