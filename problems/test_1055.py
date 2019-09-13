import unittest

import utils


# O(nm) time. O(1) space. Greedy.
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        result = 0
        si = len(source)

        for c in target:
            si = source.find(c, si) + 1
            if si == 0:
                si = source.find(c) + 1
                if si == 0:
                    return -1
                result += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().shortestWay(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
