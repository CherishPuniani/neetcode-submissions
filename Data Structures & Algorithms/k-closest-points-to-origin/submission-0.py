class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculate distance for each
        #  we have to return the points not distance
        ans = []
        res = []
        for arr in points:
            x = arr[0]
            y = arr[1]
            dist = (x**2 + y**2)**0.5
            res.append([dist,x,y])
        res.sort(key= lambda x: x[0])

        for i in range(k):
            ans.append(res[i][1:])
        return ans
