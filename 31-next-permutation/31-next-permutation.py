import heapq
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = nums[-1]
        idx = len(nums) - 1
        while(idx > 0):
            if (nums[idx-1] < nums[idx]):
                idx2 = idx
                while (idx2 < len(nums) and nums[idx2] > nums[idx-1]):
                    idx2 += 1
                nums[idx-1], nums[idx2-1] = nums[idx2-1], nums[idx-1]
                nums[idx:] = sorted(nums[idx:])
                break
            idx -= 1
        if (idx == 0):
            nums.sort()