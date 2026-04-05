class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        checkdict = {}
        for x in s:
            if(x not in checkdict):
                checkdict.update({x: 1})
            else:
                temp = checkdict[x]
                checkdict.update({x: temp + 1})
        
        for x in t:
            if(x not in checkdict):
                return False
            else:
                if(checkdict[x] == 1):
                    checkdict.pop(x)
                else:
                    temp = checkdict[x]
                    checkdict.update({x : temp - 1})
        
        return True