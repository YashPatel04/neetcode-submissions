class Solution:
    def findOrder(self, numCourses: int, preq: List[List[int]]) -> List[int]:
        visited = set()
        hashmap = {}
        # result list
        res = []
        # just for checking whether we have an element in O(1) time
        check = set()
        for i in preq:
            temp = hashmap.get(i[0], [])
            temp.append(i[1])
            hashmap[i[0]]=temp
        def dfs(course):
            if course in visited:
                return False
            temp = hashmap.get(course, [])
            if temp==[]: 
                return True
            visited.add(course)
            for i in temp:
                if not dfs(i): return False
                else:
                    if i not in check:
                        res.append(i)
                        check.add(i)
            visited.remove(course)
            return True
        
        for i in range(numCourses):
            if dfs(i):
                if i not in check:
                    res.append(i)
                    check.add(i)
            else:
                return []
        return res
