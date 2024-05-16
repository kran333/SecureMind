class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        result = True
        if len(s) == 1:
            return False
        for chrt in s:
            if chrt in "([{":
                stack.append(chrt)

            if chrt in ")}]":
                if "(" in stack and chrt == ")":
                    stack.pop(stack.index("("))
                elif "[" in stack and chrt == "]":
                    stack.pop(stack.index("["))
                elif "{" in stack and chrt == "}":
                    stack.pop(stack.index("{"))
                else:
                    result = False
        if len(stack) == 0:
            return result
        else:
            return False

# s = "{[]}"
# s = "(}"
# s = "()[]{}"
# s = "("
# s = "(()"
s = "({{{{}}}))"
sol_obj = Solution()
res = sol_obj.isValid(s)
print(res)