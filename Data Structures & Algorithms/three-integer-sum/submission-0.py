class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for idx in range(n - 2):
            # Skip duplicate values for the first element
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            # Early exit: smallest possible sum > 0
            if nums[idx] > 0:
                break

            i = idx + 1
            j = n - 1
            tar = -nums[idx]

            while i < j:
                tot = nums[i] + nums[j]

                if tot == tar:
                    ans.append([nums[idx], nums[i], nums[j]])
                    
                    i += 1
                    j -= 1

                    # Skip duplicate values for second and third elements
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif tot > tar:
                    j -= 1
                else:
                    i += 1

        return ans