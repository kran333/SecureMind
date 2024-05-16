class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = []
        k = 0
        for num in nums:
            if num not in sorted_nums:
                sorted_nums.append(num)
            else:
                k += 1
        # for _ in range(k):
        #     sorted_nums.append("_")
        return sorted_nums










# nums = [1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [0,0,1,1,1,2,2,3,3,4]
sol_obj = Solution()
res = sol_obj.removeDuplicates(nums)
print(res)