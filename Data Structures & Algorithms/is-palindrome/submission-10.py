class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) -1
        
        def alphNum(char):
            if (48 <= ord(char) <= 57) or (65 <= ord(char) <= 90) or (97 <= ord(char)<= 122 ):
                return True
            else:
                return False
        
        while l <= r:
            if alphNum(s[l]):
                if alphNum(s[r]):
                    if s[l].lower() != s[r].lower():
                        return False
                    else:
                        l += 1
                        r -=1  
                else:
                    r -=1    
            else:
                l += 1
              

        return True