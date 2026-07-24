class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in map.keys():
                print(comp)
                if i+1 < map[comp]+1:
                    return [i+1, map[comp]+1]
                else:
                    return[map[comp]+1, i+1]

            map[numbers[i]] = i