"""
https://leetcode.com/problems/count-binary-substrings/

https://leetcode.com/submissions/detail/130289823/
"""


class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for index in range(len(s) - 1):
            diff = 0
            start = index - diff
            end = index + diff + 1
            _type = None
            if s[start] == '1' and s[end] == '0':
                _type = '10'
                diff += 1
            elif s[start] == '0' and s[end] == '1':
                _type = '01'
                diff += 1
            else:
                continue
            start = index - diff
            end = index + diff + 1
            while start >= 0 and end < len(s):
                if _type == '10' and s[start] == '1' and s[end] == '0':
                    diff += 1
                elif _type == '01' and s[start] == '0' and s[end] == '1':
                    diff += 1
                else:
                    break
                start = index - diff
                end = index + diff + 1
            count += diff
        return count


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        # self.assertEqual(solution.countBinarySubstrings('00110011'), 6)
        # self.assertEqual(solution.countBinarySubstrings('10101'), 4)
        self.assertEqual(solution.countBinarySubstrings('000111000'), 6)

if __name__ == '__main__':
    unittest.main()
