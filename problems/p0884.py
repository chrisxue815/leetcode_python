import collections
import unittest
import utils


# O(n) time. O(n) space. Hash table.
class Solution(object):
    def uncommonFromSentences(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: List[str]
        """
        count_a = collections.Counter()
        count_b = collections.Counter()

        for word in a.split():
            count_a[word] += 1

        for word in b.split():
            count_b[word] += 1

        result = []

        for word, count in count_a.iteritems():
            if count == 1 and word not in count_b:
                result.append(word)

        for word, count in count_b.iteritems():
            if count == 1 and word not in count_a:
                result.append(word)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().uncommonFromSentences(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
