class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""
        str_len = len(strs[0])
        for ele in strs:
            if len(ele) < str_len:
                str_len = len(ele)
        for x in range(str_len):
            temp = ''
            for element in strs:
                if element[x] != temp:
                    pass
            print(element)
        return result


strs = ["flower","flow","flight"]
sol_obj = Solution()
res = sol_obj.longestCommonPrefix(strs)
print(res)
