class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = []
        for x in range(n + 1):
            
            count = 0
            temp = x
            while x:
                x &= x - 1
                count += 1
            ans.append(count)
        
        return ans