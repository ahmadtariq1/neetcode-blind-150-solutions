class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        stack = []
        res = [0] * len(temperatures)
        for i,x in enumerate(temperatures):

            if not stack:
                stack.append((x,i))
            else:
                while len(stack) > 0 and stack[-1][0] < x :
                    res[stack[-1][1]] = ( i - stack[-1][1])
                    stack.pop()

                    
                stack.append((x,i))



        return res