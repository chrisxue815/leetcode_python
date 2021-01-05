import unittest

import utils


# O(n) time. O(1) space. Math.
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        while True:
            length = 0
            for c in S:
                if c.isalpha():
                    length += 1
                    if length == K:
                        return c
                else:
                    multiplier = ord(c) - ord('0')
                    new_length = length * multiplier
                    if new_length >= K:
                        K = (K - 1) % length + 1
                        continue
                    length = new_length


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().decodeAtIndex(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
