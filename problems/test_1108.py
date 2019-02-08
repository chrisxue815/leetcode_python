import unittest

import utils


# O(n) time. O(1) space. String.
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().defangIPaddr(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
