import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        h = [(-nums[i], i) for i in range(k)]
        heapq.heapify(h)

        res.append(-1 * h[0][0])

        for i in range(len(nums) - k):
            heapq.heappush(h, (-nums[k + i], k + i))

            while h[0][1] <= i:
                heapq.heappop(h)

            res.append(-1 * h[0][0])

        return res