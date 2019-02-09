import io
import threading
import time
import unittest.mock

import utils


class Foo:
    def __init__(self):
        self.first_passed = threading.Event()
        self.second_passed = threading.Event()

    def first(self, printFirst):
        printFirst()
        self.first_passed.set()

    def second(self, printSecond):
        if not self.first_passed.wait(1):
            raise TimeoutError()
        printSecond()
        self.second_passed.set()

    def third(self, printThird):
        if not self.second_passed.wait(1):
            raise TimeoutError()
        printThird()


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            self.run_case(case)

    def run_case(self, case):
        def printFirst():
            print('first', end='')

        def printSecond():
            print('second', end='')

        def printThird():
            print('third', end='')

        obj = Foo()

        threads = [
            None,
            threading.Thread(target=lambda: obj.first(printFirst)),
            threading.Thread(target=lambda: obj.second(printSecond)),
            threading.Thread(target=lambda: obj.third(printThird)),
        ]

        def start_all_threads():
            for thread_id in case.thread_order:
                threads[thread_id].start()
                time.sleep(0.1)

        _, actual = self.run_with_mock_stdout(start_all_threads)

        self.assertEqual(case.expected, actual)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def run_with_mock_stdout(self, func, mock_stdout):
        result = func()
        return result, mock_stdout.getvalue()


if __name__ == '__main__':
    unittest.main()
