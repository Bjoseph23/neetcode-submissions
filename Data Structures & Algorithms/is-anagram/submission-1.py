class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for c in s:
            s_map[c] += 1

        for c in t:
            t_map[c] += 1
        
        for count in s_map:
            if s_map[count] != t_map[count]:
                return False
        return True
        

