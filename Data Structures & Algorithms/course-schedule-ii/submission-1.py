class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # map each course to it's pre-requisite
        preMap = { i:[] for i in range(numCourses) }
        # the number of courses dependant on the pre-reqs
        indegree = [0 for i in range(numCourses)]
        ans = []

        # map all courses to their prerequisites
        # also map, how many courses depend on this pre-req
        for crs, pre in prerequisites:
            indegree[pre] += 1
            preMap[crs].append(pre)

        # get all the courses that have no dependencies
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            ans = [node] + ans
            for nei in preMap[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return ans if len(ans) == numCourses else []