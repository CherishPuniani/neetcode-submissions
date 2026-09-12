from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if there is a cycle then return false?
        # map lectures to whose prereq they are?
        h_map = defaultdict(list)
        q = deque()
        ind = [0]*numCourses
        res = []
        for t in prerequisites:
            h_map[t[1]].append(t[0])
            ind[t[0]] += 1
        
        # first add to queue all with indegree 0
        for i,x in enumerate(ind):
            if x == 0:
                q.append(i)

        while(q):
            element = q.popleft()
            for t in h_map[element]:
                ind[t] -= 1
                if ind[t] == 0:
                    q.append(t)
            res.append(element)

        if len(res) == numCourses:
            return True
        
        return False
