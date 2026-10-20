class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s.lower() if c.isalnum())
        strs  = s
        res = ""
        for i in range(len(strs)-1, -1, -1):
            res += strs[i]
        
        if s == res:
            return True
            exit()
        else:
            return False
    

        