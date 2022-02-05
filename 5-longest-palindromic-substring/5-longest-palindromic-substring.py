class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        
        if (s_len == 1):
            return s
        elif (s_len == 2):
            if (s[0] == s[1]):
                return s
            else:
                return s[0]
        
        result = ""
        for i in range(1, s_len):
            left = i - 1
            right = i
            
            # even
            while (left >= 0 and right < s_len and s[left] == s[right]):
                left -= 1
                right += 1
                
            left += 1
            right -= 1
                
            if (len(result) < right - left + 1):
                result = s[left:right+1]
                
            # odd
            left = i - 2
            right = i
            while (left >= 0 and right < s_len and s[left] == s[right]):
                left -= 1
                right += 1
            
            left += 1
            right -= 1
                
            if (len(result) < right - left + 1):
                result = s[left:right+1]
                
        return result