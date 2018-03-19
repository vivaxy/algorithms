"""
https://leetcode.com/problems/replace-words/description/

https://leetcode.com/submissions/detail/145826790/
"""


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        roots = sorted(dict)
        def replaceWordInDict(successor):
            for root in roots:
                if successor.startswith(root):
                    return root
            return successor
        return ' '.join(map(lambda word: replaceWordInDict(word), sentence.split()))


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.replaceWords(
            ["cat", "bat", "rat"], "the cattle was rattled by the battery"), "the cat was rat by the bat")


if __name__ == '__main__':
    unittest.main()
