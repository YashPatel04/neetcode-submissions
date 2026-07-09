class Solution:
    def canFinish(self, numCourses: int, preq: List[List[int]]) -> bool:
        visited = set()
        hashmap = {}
        for i in preq:
            temp = hashmap.get(i[0],[])
            temp.append(i[1])
            hashmap[i[0]]=temp
        def dfs(course, visited):
            if course in visited:
                return False
            visited.add(course)
            temp = hashmap.get(course,[])
            for j in temp:
                if not dfs(j, visited): return False
            visited.remove(course)
            return True

        for i in hashmap.keys():
            val = dfs(i, visited)
            if not val: return False
        return True