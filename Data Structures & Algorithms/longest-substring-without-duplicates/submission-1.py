class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        longest = 0
        hashmap = {}
        start = 0
        for i in range(len(s)):
            if s[i] in hashmap and hashmap[s[i]] >= start:
                start = hashmap[s[i]] + 1

            hashmap[s[i]] = i
            curr_length = i - start + 1
            longest = max(curr_length, longest)

        return longest

        




        