class Solution(object):
    def romanToInt(self, s):
        look_up = {
            'I': 1,
            'V': 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        result = 0
        for index in range(1, len(s)+1):
            if look_up[s[-index]] < look_up[s[-(index+1)]]:
                result = result - look_up[s[-(index+1)]]
                print(result)
            else:
                result += look_up[s[-index]]
                print(result)
        return result


s = "MCMXCIV"
sol_obj = Solution()
res = sol_obj.romanToInt(s)
print(res)