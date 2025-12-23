class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num % 2:
                num = num - 1
            else:
                num = num / 2
            steps = steps + 1
        return steps



if __name__ == ('__main__'):
    print('sergey')
    num = 7
    print(Solution().numberOfSteps(num))


 # rep 5+

