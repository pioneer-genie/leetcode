class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if (word1 == ""):
            return len(word2)
        if (word2 == ""):
            return len(word1)
        
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        
        for i in range(len(word1)+1):
            dp[i][0] = i
        for i in range(len(word2)+1):
            dp[0][i] = i
            
        for idx1 in range(1, len(word1)+1):
            for idx2 in range(1, len(word2)+1):
                if (word1[idx1-1] == word2[idx2-1]):
                    dp[idx1][idx2] = dp[idx1-1][idx2-1]
                else:
                    insert = dp[idx1][idx2-1] + 1
                    delete = dp[idx1-1][idx2] + 1
                    replace = dp[idx1-1][idx2-1] + 1
                    dp[idx1][idx2] = min(insert, delete, replace)
        
        return dp[len(word1)][len(word2)]