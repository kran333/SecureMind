class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # nums = [1, 3, 5, 6]
        # if target in nums:
        #     return nums.index(target)
        # print(len(nums))

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

obj = Solution()
nums = [1,3,5,6,10]
target = 11

res = obj.searchInsert(nums, target)
print("return val: ", res)