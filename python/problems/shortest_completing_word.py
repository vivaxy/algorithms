"""
https://leetcode.com/problems/shortest-completing-word/

https://leetcode.com/submissions/detail/132960422/
"""

import sys

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        charDict = dict()
        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                if not char in charDict:
                    charDict[char] = 0
                charDict[char] += 1
        resultWord = ''
        resultWordLen = sys.maxsize
        for word in words:
            thisWordOK = True
            for char in charDict:
                if word.count(char) < charDict[char]:
                    thisWordOK = False
                    break
            if thisWordOK:
                wordLen = len(word)
                if wordLen < resultWordLen:
                    resultWord = word
                    resultWordLen = wordLen
        return resultWord


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.shortestCompletingWord(
            '1s3 PSt', ["step", "steps", "stripe", "stepple"]), 'steps')
        self.assertEqual(solution.shortestCompletingWord(
            '1s3 456', ["looks", "pest", "stew", "show"]), 'pest')


if __name__ == '__main__':
    unittest.main()
