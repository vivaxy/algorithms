"""
https://leetcode.com/problems/most-common-word/description/

https://leetcode.com/submissions/detail/150204402/
"""


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        wordAcc = dict()
        for word in paragraph.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('\'', '').replace(';', '').split(' '):
            if word not in banned:
                if word in wordAcc:
                    wordAcc[word] += 1
                else:
                    wordAcc[word] = 1
        maxCount = 0
        ans = ''
        for word in wordAcc:
            count = wordAcc[word]
            if count > maxCount:
                maxCount = count
                ans = word
        return ans



import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.mostCommonWord(
            'Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']), 'ball')


if __name__ == '__main__':
    unittest.main()
