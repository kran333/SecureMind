class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for num in nums2:
            nums1.append(num)
        new_list = []
        while nums1:
            min = nums1[0]
            for num in nums1:
                if min >= num:
                    min = num
            new_list.append(min)
            nums1.remove(min)
        return new_list


list1 = [1,2,4, 7]
list2 = [5,3,6]
sol_obj = Solution()
res = sol_obj.findMedianSortedArrays(list1, list2)
print(res)