import datetime
import unittest

import utils


# O(1) time. O(1) space.
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.datetime(year, month, day).strftime('%A')


class Test(unittest.TestCase):
    def test(self):
        func_name = next(f for f in dir(Solution) if not f.startswith('__'))
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            func = getattr(Solution(), func_name)
            actual = func(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
