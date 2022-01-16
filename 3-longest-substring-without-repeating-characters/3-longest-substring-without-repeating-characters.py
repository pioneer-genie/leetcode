class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        ch_set = set()
        
        p1 = p2 = 0
        while(p2 < len(s)):
            if (s[p2] in ch_set):
                max_len = max(max_len, len(ch_set))
                while(True):
                    ch_set.remove(s[p1])
                    p1 += 1
                    if (s[p1-1] == s[p2]):
                        break
            
            ch_set.add(s[p2])
            p2 += 1
            
        max_len = max(max_len, len(ch_set))
        
        return max_len