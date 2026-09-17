class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        current = 0 

        while current < len(nums):
            if nums[current] == 0:
                nums.pop(current)
                count += 1
            else:
                current +=1
        while count:
            nums.append(0)
            count -=1
        