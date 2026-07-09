class Solution:
    def canFinish(self, numCourses: int, preq: List[List[int]]) -> bool:
        visited = set()
        hashmap = {}
        for i in preq:
            temp = hashmap.get(i[0],[])
            temp.append(i[1])
            hashmap[i[0]]=temp
        def dfs(course):
            if course in visited:
                return False
            temp = hashmap.get(course,[])
            if temp==[]: return True
            visited.add(course)
            for j in temp:
                if not dfs(j): return False
            visited.remove(course)
            hashmap[course]=[]
            return True

        for i in range(numCourses):
            val = dfs(i)
            if not val: return False
        return True