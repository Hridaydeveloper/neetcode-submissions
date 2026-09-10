class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
        for i in range(len(t)):
            if t[i] in hashmap:
                hashmap[t[i]] -= 1
                if hashmap[t[i]] == 0:
                    del hashmap[t[i]] 
            else:
                return False
        else:
            return True

        