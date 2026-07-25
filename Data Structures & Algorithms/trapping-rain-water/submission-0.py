class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax, rightMax = [0] * n, [0] * n
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]
        total_water = 0

        for i in range(1, len(height)):

            leftMax[i]= (max(leftMax[i-1], height[i]))
        
        for i in range (len(height) -2, -1, -1):
            rightMax[i] = (max(rightMax[i+1], height[i]))
        
        for i in range(len(height)):
            current_Water = min(leftMax[i], rightMax[i]) - height[i]
            total_water += current_Water
        return total_water

        # height   =  [0,2,0,3,1,0,1,3,2,1]
        # leftMax  =  [0,2,2,3,3,3,3,3,3,3]
        # rightMax =  [3,3,3,3,3,3,3,3,2,1]
        # water =     [0,0,2,0,2,3,2,0,0,0] = 9
