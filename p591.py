import unittest

_CDATA_OPEN = '[CDATA['
_CDATA_CLOSE = ']]>'


# O(n) time. O(n) space.
class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        if len(code) < 7 or code[0] != '<' or code[1] == '!':
            return False

        def _check_cdata(lo):
            if not code.startswith(_CDATA_OPEN, lo):
                return False, -1
            hi = code.find(_CDATA_CLOSE, lo)
            if hi == -1:
                return False, -1
            return True, hi + len(_CDATA_CLOSE)

        def _get_tag(lo):
            hi = code.find('>', lo)
            if hi == -1 or not (1 <= hi - lo <= 9):
                return False, None, -1
            tag = code[lo:hi]
            if not tag.isalpha() or not tag.isupper():
                return False, None, -1
            return True, tag, hi + 1

        n = len(code)
        tags = []
        i = 0

        while i < n:
            ch = code[i]
            if ch == '<':
                i += 1
                if i >= n:
                    return False
                if code[i] == '!':
                    ok, i = _check_cdata(i + 1)
                    if not ok:
                        return False
                elif code[i] == '/':
                    if not tags:
                        return False
                    ok, tag, i = _get_tag(i + 1)
                    if not ok or tag != tags.pop() or (i < n and not tags):
                        return False
                else:
                    ok, tag, i = _get_tag(i)
                    if not ok:
                        return False
                    tags.append(tag)
            else:
                i += 1
        return len(tags) == 0


class Test(unittest.TestCase):
    def test(self):
        self._test('<DIV>This is the first line <![CDATA[<div>]]></DIV>', True)
        self._test('<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>', True)
        self._test('<A>  <B> </A>   </B>', False)
        self._test('<DIV>  div tag is not closed  <DIV>', False)
        self._test('<DIV>  unmatched <  </DIV>', False)
        self._test('<DIV> closed tags with invalid tag name  <b>123</b> </DIV>', False)
        self._test('<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>', False)
        self._test('<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>', False)
        self._test('<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>', False)
        self._test('<TRUe><![CDATA[123123]]]]><![CDATA[>123123]]></TRUe>', False)
        self._test('<A><A>/A></A></A>', True)
        self._test('<A<></A<>', False)

    def _test(self, code, expected):
        actual = Solution().isValid(code)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
