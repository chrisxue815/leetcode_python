import unittest


def _find_comment(line):
    for i, ch in enumerate(line):
        if ch == '/' and i + 1 < len(line):
            ch = line[i + 1]
            if ch == '/' or ch == '*':
                return i
    return -1


# O(n) time. O(1) space.
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        row = 0
        while row < len(source):
            line = source[row]
            lo = _find_comment(line)

            if lo == -1:
                row += 1
                continue

            if line[lo + 1] == '/':
                if lo == 0:
                    source.pop(row)
                else:
                    source[row] = line[:lo]
                    row += 1
                continue

            hi = line.find('*/', lo + 2)
            if hi != -1:
                if lo == 0 and hi + 2 == len(line):
                    source.pop(row)
                else:
                    source[row] = line[:lo] + line[hi + 2:]
                continue

            if lo == 0:
                source.pop(row)
            else:
                source[row] = line[:lo]
                row += 1

            while row < len(source):
                line = source[row]
                hi = line.find('*/')
                if hi == -1:
                    source.pop(row)
                    continue

                if hi + 2 == len(line):
                    source.pop(row)
                else:
                    if lo == 0:
                        source[row] = line[hi + 2:]
                    else:
                        source.pop(row)
                        row -= 1
                        source[row] += line[hi + 2:]
                break

        return source


class Test(unittest.TestCase):
    def test(self):
        self._test([
            "/*Test program */",
            "int main()",
            "{ ",
            "  // variable declaration ",
            "int a, b, c;",
            "/* This is a test",
            "   multiline  ",
            "   comment for ",
            "   testing */",
            "a = b + c;",
            "}",
        ], [
            "int main()",
            "{ ",
            "  ",
            "int a, b, c;",
            "a = b + c;",
            "}",
        ])

        self._test([
            "a/*comment",
            "line",
            "more_comment*/b",
        ], [
            "ab",
        ])

        self._test(['/*/*/1'], ['1'])
        self._test(['1/**/2//3'], ['12'])

    def _test(self, source, expected):
        actual = Solution().removeComments(source)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
