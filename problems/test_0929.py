import unittest
import utils


# O(n) time. O(n) space. Hash table.
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        normalized = set()

        for email in emails:
            local, domain = email.split('@')

            local = local.split('+', 1)[0].replace('.', '')

            normalized.add(local + '@' + domain)

        return len(normalized)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().numUniqueEmails(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
