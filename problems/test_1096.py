import itertools
import unittest
from typing import List

import utils


# Recursive descent parser, one pass.
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def parse_product(start):
            groups = []
            i = start

            while i < len(expression):
                c = expression[i]

                if c == '{':
                    i, sub = parse_list(i + 1)
                    groups.append(sub)
                elif c == '}' or c == ',':
                    break
                else:
                    groups.append(c)

                i += 1

            return i, (''.join(options) for options in itertools.product(*groups))

        def parse_list(start):
            result = set()
            i = start

            while True:
                i, sub = parse_product(i)
                result.update(sub)

                if i >= len(expression) or expression[i] == '}':
                    break

                i += 1

            return i, result

        return list(sorted(parse_product(0)[1]))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().braceExpansionII(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
