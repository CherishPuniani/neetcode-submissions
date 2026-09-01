class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        # ans = 0
        for x in range(k):
            ans = heapq.heappop_max(nums)
        return ans