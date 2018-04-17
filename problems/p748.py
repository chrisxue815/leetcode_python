import unittest
import utils


# O(n) time. O(1) space. Counting.
class Solution(object):
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
        cases = utils.load_json_from_path('../leetcode_test_cases/p748.json').test_cases

        for case in cases:
            actual = Solution().shortestCompletingWord(case.licensePlate, case.words)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
