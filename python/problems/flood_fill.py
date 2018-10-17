"""
https://leetcode.com/problems/flood-fill/

https://leetcode.com/submissions/detail/130734501/
"""


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        totalRowCount = len(image)
        totalColCount = len(image[0])
        initialValue = image[sr][sc]
        toSearchPixels = [{'row': sr, 'col': sc}]
        toUpdatePixels = []
        while len(toSearchPixels):
            centerPixel = toSearchPixels.pop()
            # up
            pixel = {'row': centerPixel['row'] - 1, 'col': centerPixel['col']}
            if pixel['row'] >= 0 and image[pixel['row']][pixel['col']] == initialValue and pixel not in toSearchPixels and pixel not in toUpdatePixels:
                toSearchPixels.append(pixel)
            # down
            pixel = {'row': centerPixel['row'] + 1, 'col': centerPixel['col']}
            if pixel['row'] < totalRowCount and image[pixel['row']][pixel['col']] == initialValue and pixel not in toSearchPixels and pixel not in toUpdatePixels:
                toSearchPixels.append(pixel)
            # left
            pixel = {'row': centerPixel['row'], 'col': centerPixel['col'] - 1}
            if pixel['col'] >= 0 and image[pixel['row']][pixel['col']] == initialValue and pixel not in toSearchPixels and pixel not in toUpdatePixels:
                toSearchPixels.append(pixel)
            # down
            pixel = {'row': centerPixel['row'], 'col': centerPixel['col'] + 1}
            if pixel['col'] < totalColCount and image[pixel['row']][pixel['col']] == initialValue and pixel not in toSearchPixels and pixel not in toUpdatePixels:
                toSearchPixels.append(pixel)
            toUpdatePixels.append(centerPixel)
        for pixel in toUpdatePixels:
            image[pixel['row']][pixel['col']] = newColor
        return image


import unittest


class Test(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.floodFill(
            [[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]])


if __name__ == '__main__':
    unittest.main()
