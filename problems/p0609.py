import unittest
import collections


class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)

        for path in paths:
            parts = path.split(' ')
            dir = parts[0]
            for file in parts[1:]:
                file_parts = file.split('(')
                d[file_parts[1]].append(dir + '/' + file_parts[0])

        return [files for files in d.itervalues() if len(files) > 1]


class Test(unittest.TestCase):
    def test(self):
        self._test(
            ['root/a 1.txt(abcd) 2.txt(efgh)', 'root/c 3.txt(abcd)', 'root/c/d 4.txt(efgh)', 'root 4.txt(efgh)'],
            [['root/a/2.txt', 'root/c/d/4.txt', 'root/4.txt'], ['root/a/1.txt', 'root/c/3.txt']])

    def _test(self, paths, expected):
        actual = Solution().findDuplicate(paths)
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
