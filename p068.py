import unittest


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        lo = 0
        line_len = len(words[0])

        for hi in xrange(1, len(words)):
            word = words[hi]
            new_len = line_len + len(word)

            if new_len + hi - lo <= maxWidth:
                line_len = new_len
            else:
                num_spans = hi - lo - 1
                total_spaces = maxWidth - line_len

                if num_spans == 0:
                    lines.append(words[lo] + ' ' * total_spaces)
                else:
                    spaces_per_span = total_spaces // num_spans
                    extra_space = total_spaces % num_spans
                    spaces = ' ' * (spaces_per_span + 1)
                    line = spaces.join(words[lo:lo + extra_space + 1])
                    spaces = ' ' * spaces_per_span
                    line += spaces + spaces.join(words[lo + extra_space + 1:hi])
                    lines.append(line)

                lo = hi
                line_len = len(word)

        extra_spaces = maxWidth - (line_len + len(words) - 1 - lo)
        lines.append(' '.join(words[lo:]) + ' ' * extra_spaces)
        return lines


class Test(unittest.TestCase):
    def test(self):
        self._test(['This', 'is', 'an', 'example', 'of', 'text', 'justification.'],
                   16,
                   [
                       'This    is    an',
                       'example  of text',
                       'justification.  '
                   ])

        self._test(['This', 'is', 'an', 'example', 'of', 'good', 'python', 'code', ':)'],
                   16,
                   [
                       'This    is    an',
                       'example  of good',
                       'python code :)  '
                   ])

        self._test(['a', 'b'], 1, ['a', 'b'])
        self._test(['aa', 'bb'], 2, ['aa', 'bb'])
        self._test(['aa', 'bb'], 3, ['aa ', 'bb '])

    def _test(self, words, maxWidth, expected):
        actual = Solution().fullJustify(words, maxWidth)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
