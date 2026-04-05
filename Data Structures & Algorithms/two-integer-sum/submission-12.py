class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num1 = 0
        num2 = 0
        checkdict = {}
        for x in nums:
            if(x not in checkdict):
                checkdict[x] = 1
            else:
                temp = checkdict[x]
                checkdict.update({x: temp + 1})
        for x in nums:
            if(checkdict[x] == 1):
                checkdict.pop(x)
            elif(checkdict[x] >1):
                temp = checkdict[x]
                checkdict.update({x:temp-1 })
            
            temp = target - x
            if(temp in checkdict):
                num1 = x
                num2 = temp
                break
            if(x not in checkdict):
                checkdict.update({x: 1})
            else:
                temp = checkdict[x]
                checkdict.update({x:temp+1 })
            
        print("num1: " + str(num1))
        print("num2: " + str(num2))
        index1 = 0
        index2 = 0
        for i,x in enumerate(nums):
            if(x == num1):
                index1 = i
                print("index1: " + str(index1))
                break
        for i,x in enumerate(nums):
            if(x == num2 and i != index1):
                index2 = i
                print("index2: " + str(index2))
                break
        
        if(index1 > index2):
            return [index2, index1]
        else:
            return [index1, index2]
                
        

