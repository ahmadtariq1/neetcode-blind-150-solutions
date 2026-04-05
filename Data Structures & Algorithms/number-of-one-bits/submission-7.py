class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0

        for i in range(31 , - 1, - 1):
            if(n == 1):
                count += 1
                return count
            print("i: " + str(i))
            if(n // (pow(2,i)) == 1):
                count += 1
                n = n % (pow(2,i))
        
        return count