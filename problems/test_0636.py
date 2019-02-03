import unittest


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            parts = log.split(':')
            func = int(parts[0])
            time = int(parts[2])
            if parts[1] == 'end':
                time += 1
                result[func] += time - prev_time
                stack.pop()
            else:
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(func)
            prev_time = time

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(2, [
            '0:start:0',
            '1:start:2',
            '1:end:5',
            '0:end:6',
        ], [3, 4])

    def _test(self, n, logs, expected):
        actual = Solution().exclusiveTime(n, logs)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
