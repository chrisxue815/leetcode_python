import unittest
import utils


# O(n) time. O(n) space. Hash table.
class Solution(object):
    def numSpecialEquivGroups(self, a):
        """
        :type a: List[str]
        :rtype: int
        """
        groups = set()

        for s in a:
            even_count = [0] * 26
            odd_count = [0] * 26
            for i in range(0, len(s), 2):
                even_count[ord(s[i]) - ord('a')] += 1
            for i in range(1, len(s), 2):
                odd_count[ord(s[i]) - ord('a')] += 1
            groups.add(tuple(even_count + odd_count))

        return len(groups)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().numSpecialEquivGroups(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
