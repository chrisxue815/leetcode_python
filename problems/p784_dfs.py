import unittest
import utils

upper_a = ord('A')
upper_z = ord('Z')
lower_a = ord('a')
lower_z = ord('z')


# O(2^n) time. O(n) space. DFS.
class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = list(s)
        result = []

        def dfs(index):
            if index == len(s):
                result.append(''.join(s))
                return

            dfs(index + 1)
            ch = ord(s[index])
            if upper_a <= ch <= upper_z:
                s[index] = chr(ch - upper_a + lower_a)
                dfs(index + 1)
                s[index] = chr(ch)
            elif lower_a <= ch <= lower_z:
                s[index] = chr(ch - lower_a + upper_a)
                dfs(index + 1)
                s[index] = chr(ch)

        dfs(0)
        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p784.json').test_cases

        for case in cases:
            actual = Solution().letterCasePermutation(case.s)
            self.assertItemsEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
