class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text =[]
        for char in s:
            if char.isalnum():
                cleaned_text+= char.lower()
                
        l=0
        r=len(cleaned_text) -1
        while l <= r:
            if cleaned_text[l] != cleaned_text[r]:
                return False
            else:
                l += 1
                r -= 1
        return True