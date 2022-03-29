class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        
        if (len(nums) < 3):
            return []
        
        left = 0
        while(left < len(nums) - 2):
            right = len(nums)-1
            mid = left + 1
            while(mid < right):
                if (nums[left] + nums[mid] + nums[right]) == 0:
                    result.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    while ( mid < right ) and (nums[mid-1] == nums[mid]):
                        mid += 1
                elif (nums[left] + nums[mid] + nums[right]) > 0:
                    right -= 1
                elif (nums[left] + nums[mid] + nums[right]) < 0:
                    mid += 1
                    
            left += 1
            while ( left < right - 1 ) and (nums[left-1] == nums[left]):
                left += 1
                
        return result