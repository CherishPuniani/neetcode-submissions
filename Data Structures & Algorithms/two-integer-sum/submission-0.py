# from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # as the nums.length is small we can create a hash map
        # h_dict = defaultdict(int)
        h_dict = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req in h_dict:
                return [h_dict[req],i]
            h_dict[nums[i]] = i
