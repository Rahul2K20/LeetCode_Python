#Naive 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        return cleaned == cleaned[::-1]
    
#Optimal
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, h = 0, len(s)-1 
        while (l<h):
            if s[l].lower() == s[h].lower():
                l+=1 
                h-=1 
            elif not s[l].isalnum():
                l+=1 
            elif not s[h].isalnum():
                h-=1 
            else: 
                return False 
        return True 