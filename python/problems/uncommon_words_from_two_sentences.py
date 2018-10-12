"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

https://leetcode.com/submissions/detail/182166803/
"""


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        apt = dict()

        def traverse(sentence):
            for word in sentence.split(' '):
                if word in apt:
                    apt[word] += 1
                else:
                    apt[word] = 1
        traverse(A)
        traverse(B)
        ans = []
        for word in apt:
            if apt[word] == 1:
                ans.append(word)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.uncommonFromSentences(
            "this apple is sweet", "this apple is sour"),
            ["sweet", "sour"]
        )
        self.assertEqual(solution.uncommonFromSentences(
            "apple apple", "banana"),
            ["banana"]
        )


if __name__ == '__main__':
    unittest.main()
