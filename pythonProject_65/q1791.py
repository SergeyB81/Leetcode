from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges [1]:
            return edges[0][0]
        else: return edges[0][1]

    def findCenter1(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()





if __name__ == '__main__':
    print('sergey')
    edges = [[1,2],[5,1],[1,3],[1,4]]
    print(Solution().findCenter1(edges))


#rep5
