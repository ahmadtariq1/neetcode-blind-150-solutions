import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = s.lower()

        text = ''.join(char for char in temp if char.isalnum())

        end = len(text) - 1
        print(end)
        for i,x in enumerate(text):
            print("i: " + str(i) + " " +"end: " + str(end) + " [i]: " + str(x) + " " + "[end]: " + str(text[end]) + " ")
            if(i == end ):
                return True
            elif(text[i] != text[end]):
                return False
                
            end = end - 1
            
            

        return True
        