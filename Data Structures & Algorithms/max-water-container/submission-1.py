class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        max_water = 0

        while l < r:
            curr_max = (r-l) * min(heights[l], heights[r])
            max_water = max(max_water, curr_max)
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] >= heights[r]:
                r-=1
        return max_water
            
