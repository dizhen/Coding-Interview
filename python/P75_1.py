class Solution(object):
    def sortColors(self, nums):
        if nums == []:
            return nums
        p0 = 0
        p2 = len(nums)-1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1