# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        final_list = lis
        # print(final_list)
        # for x in list2:
        #     list1.append(x)
        new_list = []
        while final_list:
            min = final_list[0]
            for x in final_list:
                if x <= min:
                    min = x
            new_list.append(min)
            final_list.remove(min)
        return new_list




list1 = [1,2,4, 7]
list2 = [0, 1,3,4]
sol_obj = Solution()
res = sol_obj.mergeTwoLists(list1, list2)
print(res)