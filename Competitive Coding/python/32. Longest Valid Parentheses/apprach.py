class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count = 0
        stack_a = [-1]
        i = 0 
        while(i>=0 and i<len(s)):
            if (s[i] == '('):
                stack_a.append(i)
            else:   
                stack_a.pop()
                if(len(stack_a) == 0):
                    stack_a.append(i)
                else:
                    count = max(count, i-stack_a[-1])
            i+=1
        return count
                


        