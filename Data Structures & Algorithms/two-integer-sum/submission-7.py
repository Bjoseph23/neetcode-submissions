class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = defaultdict(int)

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in lookup:
                return [lookup[complement], i]
            lookup[nums[i]] = i