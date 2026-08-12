class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to it's pre-requisite
        preMap = { i:[] for i in range(numCourses) }
        # all courses visited along the current dfs path.
        visitSet = set()

        # map all courses to their prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(course):
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True

            visitSet.add(course)
            for pre in preMap[course]:
                # if this pre-req is already visited, then there is a cycle
                if not dfs(pre):
                    return False
            # after we visit all it's pre-reqs
            visitSet.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True