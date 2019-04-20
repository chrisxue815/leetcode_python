import unittest
import utils


# O(nlog(n)) time. O(n) space. Sorting.
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, words = log.split(' ', 1)

            if words[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((words, identifier, log))

        letter_logs.sort()
        result = [log for words, identifier, log in letter_logs]
        result += digit_logs

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().reorderLogFiles(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
