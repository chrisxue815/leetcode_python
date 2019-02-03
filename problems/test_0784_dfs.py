import unittest
import utils


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

            ch = s[index]
            if ch.isupper():
                s[index] = ch.lower()
                dfs(index + 1)
                s[index] = ch
            elif ch.islower():
                s[index] = ch.upper()
                dfs(index + 1)
                s[index] = ch

        dfs(0)
        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().letterCasePermutation(**case.args._asdict())
            self.assertCountEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
