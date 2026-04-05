class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for x in s:
            if(x == '(' or x == '{' or x == '['):
                stack.append(x)
            elif(x == ')' and len(stack) != 0):
                if(stack[-1] == "("):
                    stack.pop()
                else:
                    stack.append(x)
            elif(x == '}' and len(stack) != 0):
                if(stack[-1] == "{"):
                    stack.pop()
                else:
                    stack.append(x)
            elif(x == ']' and len(stack) != 0):
                if(stack[-1] == "["):
                    stack.pop()
                else:
                    stack.append(x)
            else:
                stack.append(x)
            
        if(len(stack) == 0):
            return True
        
        return False