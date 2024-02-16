class Solution:
    def maxArea(self, height: List[int]) -> int:
        # It has a time complexity of O(n) and space complexity of O(1)
        l = 0
        r = len(height)- 1
        max_area = 0
        while l < r:
            current_area = min(height[l], height[r]) * (r-l)
            # upadate the max_area with the larger area
            if max_area < current_area:
                max_area = current_area
            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        return max_area