"""
https://leetcode.com/problems/add-binary/

https://leetcode.com/submissions/detail/106524947/
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length = max(len(a), len(b))
        remaining = 0
        index = 0
        result = ''
        while index < length:
            bit1 = 0
            if len(a) > index:
                bit1 = int(a[len(a) - index - 1])
            bit2 = 0
            if len(b) > index:
                bit2 = int(b[len(b) - index - 1])
            sum_value = bit1 + bit2 + remaining
            remaining = 0
            if sum_value > 1:
                remaining = 1
                sum_value = sum_value - 2
            result = str(sum_value) + result
            index += 1
        if remaining != 0:
            result = str(1) + result
        return result


import unittest


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().addBinary('11', '1'), '100')


if __name__ == '__main__':
    unittest.main()
