import unittest

import utils


# O(n) time. O(1) space. Math.
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        length = 0

        for c in S:
            if c.isalpha():
                length += 1
            else:
                length *= ord(c) - ord('0')

        for c in reversed(S):
            if c.isalpha():
                if length == K:
                    return c
                length -= 1
            else:
                length /= ord(c) - ord('0')
                K = (K - 1) % length + 1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().decodeAtIndex(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
