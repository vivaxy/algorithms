"""
https://en.wikipedia.org/wiki/Levenshtein_distance

    s t r i n g A
  0 1 2 3 4 5 6 7
s 1 ?
t 2
r 3
i 4
n 5
g 6
B 7

"""


class Levenshtein(object):
    def __init__(self, stringA, stringB):
        self.stringA = stringA
        self.stringB = stringB
        matrix = [list(range(0, len(stringA) + 1))]
        for i in range(len(stringB)):
            row = [i + 1]
            for j in range(len(stringA)):
                value = min(matrix[i - 1][j] + 1, row[j - 1] + 1)
                diff = 0 if stringB[i] == stringA[j] else 1
                value = min(value, matrix[i - 1][j - 1] + diff)
                row.append(value)
            matrix.append(row)
        self.matrix = matrix

    def getDistance(self):
        return self.matrix[len(self.stringB)][len(self.stringA)]


import unittest


class Test(unittest.TestCase):
    def test(self):
        levenshtein = Levenshtein('kitten', 'sitting')
        self.assertEqual(levenshtein.getDistance(), 3)
        levenshtein = Levenshtein('GUMBO', 'GAMBOL')
        self.assertEqual(levenshtein.getDistance(), 2)
        levenshtein = Levenshtein('', 'abcde')
        self.assertEqual(levenshtein.getDistance(), 5)
        levenshtein = Levenshtein('abcdef', '')
        self.assertEqual(levenshtein.getDistance(), 6)


if __name__ == '__main__':
    unittest.main()
