import unittest


class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 11:
            return []

        chars = ['A', 'C', 'G', 'T']
        nums = [0] * 20
        nums[2] = 1
        nums[6] = 2
        nums[19] = 3

        num = 0
        for ch in s[9::-1]:
            num = num << 2 | nums[ord(ch) - ord('A')]

        dupes = set()
        existing = {num}
        for ch in s[10:]:
            num = num >> 2 | nums[ord(ch) - ord('A')] << 18
            if num in existing:
                dupes.add(num)
            existing.add(num)

        result = [None] * len(dupes)
        i = 0
        for num in dupes:
            s = []
            for _ in range(10):
                s.append(chars[num & 3])
                num >>= 2
            result[i] = ''.join(s)
            i += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT', [
            'AAAAACCCCC',
            'CCCCCAAAAA',
        ])

    def _test(self, s, expected):
        actual = Solution().findRepeatedDnaSequences(s)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
