class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        dict = {}

        for x in nums:
            if(x not in dict):
                dict[x] = 1
            else:
                dict[x] += 1
        
        #data = [[]] * n
        data = [[] for _ in range(n + 1)]
        for x in dict:
            data[dict[x]].append(x)
        
        ans = []
        for i,x in enumerate(data[::-1]):
            for y in x:
                if len(ans) == k:
                    return ans
                else:
                    ans.append(y)

        return ans
