"""
https://leetcode.com/problems/letter-case-permutation/

https://leetcode.com/submissions/detail/142553115/
"""


class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        letters = 'abcdefghijklmnopqrstuvwxyz'

        def traverse(tempAns, nextIndex):
            if nextIndex >= len(S):
                return ans.append(tempAns)
            nextChar = S[nextIndex]
            if letters.find(nextChar.lower()) == -1:
                return traverse(tempAns + nextChar, nextIndex + 1)
            traverse(tempAns + nextChar.lower(), nextIndex + 1)
            traverse(tempAns + nextChar.upper(), nextIndex + 1)
        traverse('', 0)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.letterCasePermutation('C'), ['c', 'C'])
        self.assertEqual(solution.letterCasePermutation(
            'a1b2'), ["a1b2", "a1B2", "A1b2", "A1B2"])
        self.assertEqual(solution.letterCasePermutation('3z4'), ["3z4", "3Z4"])
        self.assertEqual(solution.letterCasePermutation('12345'), ["12345"])


if __name__ == '__main__':
    unittest.main()
