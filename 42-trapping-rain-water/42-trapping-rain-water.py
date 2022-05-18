class Solution:
    def trap(self, height: List[int]) -> int:
        forward = [0 for i in range(len(height))]
        backward = [0 for i in range(len(height))]
        
        high = 0
        for i in range(len(height)):
            high = max(high, height[i])
            forward[i] = max(0, high - height[i])
        
        high = 0
        for i in reversed(range(len(height))):
            high = max(high, height[i])
            backward[i] = high - height[i]
            
        ret = 0
        for i in range(len(height)):
            ret += min(forward[i], backward[i])
            
        return ret