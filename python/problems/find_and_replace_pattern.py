"""
https://leetcode.com/problems/find-and-replace-pattern/

https://leetcode.com/submissions/detail/175947780/
"""


class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []

        def tryWord(word):
            dic = dict()
            inDicChars = list()
            for i in range(len(word)):
                if pattern[i] in dic:
                    if dic[pattern[i]] != word[i]:
                        return False
                    continue
                if word[i] in inDicChars:
                    return False
                dic[pattern[i]] = word[i]
                inDicChars.append(word[i])
            ans.append(word)
        for word in words:
            tryWord(word)

        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.findAndReplacePattern(
            ["abc", "deq", "mee", "aqq", "dkd", "ccc"], 'abb'), ["mee", "aqq"])


if __name__ == '__main__':
    unittest.main()
