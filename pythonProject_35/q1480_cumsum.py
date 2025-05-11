from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cumsum = []
        s = 0
        for el in nums:
            s = s + el
            cumsum.append(s)
        return cumsum

if __name__ == '__main__':
    print('sergey')

    nums = [1,2,3]

    l = Solution()
    print(l.runningSum(nums))


    def runningSum(nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

    # rep 1


    print(runningSum(nums))
