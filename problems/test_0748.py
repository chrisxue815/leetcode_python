import unittest
import utils


# O(n) time. O(1) space. Counting.
class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        license_counts = [0] * 26

        for ch in licensePlate:
            if ch.isalpha():
                license_counts[ord(ch.lower()) - ord('a')] += 1

        num_letters = sum(license_counts)
        result = None

        for word in words:
            counts = list(license_counts)
            num_remaining = num_letters
            for ch in word:
                ch = ord(ch) - ord('a')
                if counts[ch] == 0:
                    continue

                num_remaining -= 1
                if num_remaining == 0:
                    if not result or len(word) < len(result):
                        result = word
                    break

                counts[ch] -= 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().shortestCompletingWord(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
