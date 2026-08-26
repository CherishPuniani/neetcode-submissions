class Solution:
    def find_pivot(self, nums: List[int]):
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return l

    def search(self, nums: List[int], target: int) -> int:
        # To find valid part
        l = 0
        n = len(nums)
        r = n - 1
       
        pivot = self.find_pivot(nums)
        if target == nums[pivot]:
            return pivot

        if target <= nums[-1]:
            l, r = pivot, n - 1
        else:
            l, r = 0, pivot - 1

        while l <= r:
            mid = (r + l)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid -1
            else:
                return mid

        return -1
