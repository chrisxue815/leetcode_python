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

            plus = local.find('+')
            if plus != -1:
                local = local[:plus]

            local = local.replace('.', '')

            normalized.add(local + '@' + domain)

        return len(normalized)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p929.json').test_cases

        for case in cases:
            actual = Solution().numUniqueEmails(case.emails)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
