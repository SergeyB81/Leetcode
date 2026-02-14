class Solution:
    def maxDepth(self, s: str ) -> int:
        depth = [0]
        for i, char in enumerate(s):
            depth.append(s[:i].count('(') - s[:i].count(')'))
        return max(depth)

    def maxDepth1(self, s: str) -> int:
        res = []
        cnt = 0
        for cur in s:
            if cur == '(':
                cnt += 1
            res.append(cnt)
            if cur == ')':
                cnt -= 1
        return max(res)





if __name__ == '__main__':
    print('sergey')
    s = "(1+(2*3)+((8)/4))+1"
    print(Solution().maxDepth1(s))