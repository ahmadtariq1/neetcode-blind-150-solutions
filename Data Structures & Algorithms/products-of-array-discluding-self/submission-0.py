class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        product = 1
        for i,x in enumerate(nums):
            
            prefix[i] = product
            product = product * x

        product = 1
        for i,x in enumerate(nums[::-1]):
            
            suffix[i] = product
            product = product * x
        
        ans = []
        r_suffix = suffix[::-1]

        for i,x in enumerate(prefix):
            ans.append(prefix[i] * r_suffix[i])
        
        return ans