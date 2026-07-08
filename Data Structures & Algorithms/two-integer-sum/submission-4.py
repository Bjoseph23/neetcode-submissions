class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = defaultdict(list)
        result = []
        for i in range(len(nums)):
            hash[i] = nums[i]
        print(hash.items())

        for i in range(len(nums)):
            complement = target - nums[i]
            for index, value in hash.items():
                if value == complement and index != i:
                    result += [i]
                    result += [index]
                    return sorted(result)