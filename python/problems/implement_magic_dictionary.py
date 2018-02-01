"""
https://leetcode.com/problems/implement-magic-dictionary/description/


"""


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        alphabeta = 'abcdefghijklmnopqrstuvwxyz'
        for word in dict:
            for index in range(len(word)):
                for letter in alphabeta:
                    if letter != word[index]:
                        self.s.add(word[:index] + letter + word[index + 1:])

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return word in self.s


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)


import unittest


class Test(unittest.TestCase):
    def test(self):
        magicDictionary = MagicDictionary()
        magicDictionary.buildDict(['hello', 'leetcode'])
        self.assertEqual(magicDictionary.search('hello'), False)
        self.assertEqual(magicDictionary.search('hhllo'), True)
        self.assertEqual(magicDictionary.search('hell'), False)
        self.assertEqual(magicDictionary.search('leetcoded'), False)


if __name__ == '__main__':
    unittest.main()
