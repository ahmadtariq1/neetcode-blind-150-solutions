class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        dict = {}
        for x in nums:
            dict[x] = 1
        max = 1
        i = 0

        while i < len(nums):
            if ( nums[i] - 1 not in dict):
                count = 0
                check = True
                while(check):
                    count += 1
                    if((nums[i] + count) not in dict):
                        check = False
                if count > max:
                    max = count
                i += 1
            else:
                i += 1
        return max
        