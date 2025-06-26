
from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        gaps = []
        n = len(points)
        for i in range(1,n):
            gaps.append(points[i][0] - points[i-1][0])

        return max(gaps)

    def maxWidthOfVerticalArea1(self, points: List[List[int]]) -> int:
        A = sorted(x for x,y in points)

        return max( [b - a for a,b in zip(A, A[1:])] + [0])


    # rep5





if __name__ == ('__main__'):
    print('sergey')
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    print(Solution().maxWidthOfVerticalArea1(points))
