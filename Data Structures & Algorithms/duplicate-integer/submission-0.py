class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for x in nums:
            if(x not in check):
                check.add(x)
            else:
                return True
        return False
            
        
       