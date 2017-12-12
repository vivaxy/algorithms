"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

https://leetcode.com/submissions/detail/131676021/
"""


class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        dic = 'abcdefghijklmnopqrstuvwxyz'
        targetIndex = dic.index(target)
        resultIndex = 0
        found = False
        for i in range(len(letters)):
            letter = letters[i]
            letterIndex = dic.index(letter)
            if letterIndex <= targetIndex:
                resultIndex = i
            else:
                found = True
                resultIndex = i
                break
        if found:
            return letters[resultIndex]
        return letters[0]


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.nextGreatestLetter(
            ['c', 'f', 'j'], 'a'), 'c')
        self.assertEqual(solution.nextGreatestLetter(
            ['c', 'f', 'j'], 'c'), 'f')
        self.assertEqual(solution.nextGreatestLetter(
            ['c', 'f', 'j'], 'k'), 'c')


if __name__ == '__main__':
    unittest.main()
