class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if(nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid
        
        x = self.binsearch(nums , 0 , left - 1  , target )
        print('Second segment')
        y = self.binsearch(nums , left , len(nums) - 1 , target)

        if(x != -1):
            return x
        elif(y != -1):
            return y
        else:
            return -1
    
    def binsearch(self , nums: list[int] , left , right , target)-> int:
        print(nums[left:right])

        while left < right:
            mid = (left + right) // 2
            print(mid)

            if(nums[mid] < target):
                left = mid + 1
            else:
                right = mid
        
        print(nums[left])
        if(nums[left] == target ):
            return left
        else:
            return -1
        