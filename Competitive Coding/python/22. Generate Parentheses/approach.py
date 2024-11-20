class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = [] 

        def generate(left, right, current_string):
            if (left == right and right == n):
                result.append(current_string)
                return

            if left < n:
                generate(left+1, right, current_string+'(')
            if (left > right):
                generate(left, right+1, current_string+')')    
        generate(0 , 0, '')
            
        return result