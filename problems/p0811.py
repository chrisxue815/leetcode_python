import collections
import unittest
import utils


# O(n) time. O(n) space. Hash table.
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counter = collections.Counter()

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            count = int(count)

            while True:
                counter[domain] += count
                index = domain.find('.')
                if index == -1:
                    break
                domain = domain[index + 1:]

        return ['{} {}'.format(count, domain) for domain, count in counter.iteritems()]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().subdomainVisits(case.cpdomains)
            self.assertItemsEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
