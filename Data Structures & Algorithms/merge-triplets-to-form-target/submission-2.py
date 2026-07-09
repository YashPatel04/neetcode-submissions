class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # for i in triplets:
        #     i.sort()
        # target.sort()
        # triplets.sort(key = lambda x:x[0])
        if len(triplets)==0: return False
        if len(triplets)==1: return triplets[0]==target
        i = 0
        j = len(triplets)-1
        while i<j and j<len(triplets):
            one = triplets[i]
            two = triplets[j]
            if (one[0]>target[0] or one[1]>target[1] or one[2]>target[2]):
                i+=1
            elif (two[0]>target[0] or two[1]>target[1] or two[2]>target[2]):
                j-=1
            elif target==[max(one[0],two[0]), max(one[1],two[1]), max(one[2],two[2])]:
                return True
            else:
                one = [max(one[0],two[0]), max(one[1],two[1]), max(one[2],two[2])]
                triplets[i]=one
                j-=1
        return False