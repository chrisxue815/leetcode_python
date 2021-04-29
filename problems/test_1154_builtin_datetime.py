import datetime
import unittest

import utils


# O(1) time. O(1) space.
class Solution:
    def dayOfYear(self, date: str) -> int:
        return datetime.datetime.strptime(date, '%Y-%m-%d').timetuple().tm_yday


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().dayOfYear(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
