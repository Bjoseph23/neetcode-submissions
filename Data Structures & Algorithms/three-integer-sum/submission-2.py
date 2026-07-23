class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1] :
                continue

            low, high = i+1, len(nums) - 1
            if nums[i] > 0:
                return res

            while low < high:

                current_sum = nums[i] + nums[low] + nums[high]
                
                
                if current_sum < 0:
                    low += 1
                
                elif current_sum > 0 :
                    high -= 1
                
                else:
                    res += [[nums[i], nums[low], nums[high]]]
                    low += 1
                    high -= 1
                    
                    # Skip duplicate values on the left.
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    
                    # Skip duplicate values on the right.
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1                    
                    
                    
        return res
