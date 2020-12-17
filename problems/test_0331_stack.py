import unittest

import utils


# O(n) time. O(log(n)) space. Stack.
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = [False]
        i = 0

        while i < len(preorder):
            if preorder[i] == '#':
                while stack and stack[-1]:
                    stack.pop()
                if not stack:
                    return False
                stack[-1] = True
                i += 2
            else:
                stack.append(False)
                i += 1
                while i < len(preorder) and preorder[i] != ',':
                    i += 1
                i += 1

        return len(stack) == 1 and stack[0]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().isValidSerialization(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
