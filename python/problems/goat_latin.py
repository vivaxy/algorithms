"""
https://leetcode.com/problems/goat-latin/description/

https://leetcode.com/submissions/detail/183971202/
"""


class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = ['a', 'e', 'i', 'o', 'u']
        ans = ''
        words = S.split(' ')
        for wordIndex in range(len(words)):
            if wordIndex:
                ans += ' '
            if words[wordIndex][0].lower() in vowel:
                ans += words[wordIndex]
            else:
                ans += words[wordIndex][1:] + words[wordIndex][0]
            ans += 'ma' + 'a' * (wordIndex + 1)
        return ans


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.toGoatLatin(
            "I speak Goat Latin"), "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
        self.assertEqual(solution.toGoatLatin("The quick brown fox jumped over the lazy dog"),
                         "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
        self.assertEqual(solution.toGoatLatin("Each word consists of lowercase and uppercase letters only"),
                         "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa")


if __name__ == '__main__':
    unittest.main()
