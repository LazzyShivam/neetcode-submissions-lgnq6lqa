from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        id = [0]*numCourses
        l = [[] for i in range(numCourses)]
        q = deque()
        for a in prerequisites:
            id[a[1]]+=1
            l[a[0]].append(a[1])

        for i in range(numCourses):  
            if id[i] == 0:  
                q.append(i)
        
        while q:
            v = q.popleft()
            for j in l[v]:
                id[j]-=1
                if id[j] == 0:
                    q.append(j)

        if 1 in id:
            return False
        return True                









            
        