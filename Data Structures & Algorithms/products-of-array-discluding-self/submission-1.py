class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProd = 1
        z_cnt = 0
        for num in nums:
            if num != 0:
                totalProd *= num
            else:
                z_cnt += 1

        if z_cnt > 1:  return [0]*len(nums)

        ans = []
        for t in nums:
            if z_cnt == 0:
                ans.append(totalProd // t)
            else:
                if t == 0:
                    ans.append(totalProd)
                else:
                    ans.append(0)

        return ans