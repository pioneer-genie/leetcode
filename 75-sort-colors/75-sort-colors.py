class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(len(nums)):
            idx = 0
            changed = False
            while(idx < len(nums) - 1):
                if (nums[idx] > nums[idx+1]):
                    nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
                    changed = True
                idx += 1
            if not (changed):
                break