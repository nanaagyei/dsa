"""
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.
"""

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        rows, cols = len(image), len(image[0])

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return

            image[r][c] = color

            # Explore all four directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        dfs(sr, sc)
        return image


# Example usage:
solution = Solution()
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr, sc = 1, 1
color = 2
result = solution.floodFill(image, sr, sc, color)
print(result)  # Expected output: [[2,2,2],[2,2,0],[2,0,1]]
