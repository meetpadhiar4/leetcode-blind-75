class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = float('-inf')
        while left < right:
            curr_area = (right - left) * min(height[left], height[right])
            max_area = max(curr_area, max_area)
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                right -= 1
                
        return max_area
