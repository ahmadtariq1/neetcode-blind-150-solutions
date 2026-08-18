class Solution:
    def climbStairs(self, n: int) -> int:



        arr = [0] * (n + 1)
        arr[0] = 1
        for i in range(n + 1):
  
            if i + 1 < n + 1: 
                arr[i + 1] += arr[i]
            
            if i + 2 < n + 1:
                arr[i + 2] += arr[i]

        return arr[n]
            