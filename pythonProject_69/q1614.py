class Solution:
    def maxDepth(self, s: str) -> int:
        depth =[0]
        for i, char in enumerate(s):
            depth.append(s[:i].count('(') - s[:i].count(')'))
        return max(depth)
               # sum[1 if c == '(' else 0 -1 if c == ')' else 0]

class Solution1:
    def maxDepth(self, s: str) -> int:
        res = cur = 0
        for c in s:
            if c == '(':
                cur += 1
                res = max(res, cur)
            if c == ')':
                cur -= 1
        return res



if __name__ == '__main__':
    print('sergey')
    s = "(1+(2*3)+((8)/4))+1"
    print(Solution().maxDepth(s))

#rep5+cd
