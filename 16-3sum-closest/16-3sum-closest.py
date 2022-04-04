class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res_num = sum(nums[:3])
        diff_min = abs(target - res_num)
        for idx in range(len(nums) - 2):
            left = idx + 1
            right = len(nums) - 1
            while(left < right):
                temp_sum = nums[idx] + nums[left] + nums[right]
                if (diff_min > abs(target - temp_sum)):
                    res_num = temp_sum
                    diff_min = abs(target - temp_sum)
                    
                if (temp_sum > target):
                    right -= 1
                elif (temp_sum < target):
                    left += 1
                else:
                    # 0
                    return target
        return res_num
                    