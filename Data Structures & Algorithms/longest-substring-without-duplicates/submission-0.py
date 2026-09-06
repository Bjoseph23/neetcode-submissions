class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l=0
        longest_ss = 0

        for r in range(len(s)):
            curr_longest = 0
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            
            seen.add(s[r])
            curr_longest = (r-l)+1
            longest_ss = max(curr_longest, longest_ss)
        return longest_ss