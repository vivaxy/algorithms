"""
https://leetcode.com/problems/unique-email-addresses/

https://leetcode.com/submissions/detail/186313168/
"""


class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s = set()
        for email in emails:
            r = ''
            state = 0  # 0: starting, 1: omitting, 2: domain
            for char in email:
                if state == 0:
                    if char == '.':
                        continue
                    if char == '@':
                        state = 2
                        r += char
                        continue
                    if char == '+':
                        state = 1
                        continue
                    r += char
                    continue
                elif state == 1:
                    if char == '@':
                        state = 2
                        r += char
                        continue
                    continue
                r += char
            s.add(r)
        return len(s)


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.numUniqueEmails(
            ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]), 2)


if __name__ == '__main__':
    unittest.main()
