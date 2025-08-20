from math import factorial


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        n = len(nums)
        pairs = []
        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j] and i < j:
                    pairs.append((i, j))
        return (pairs)  # на литкоде len(pairs)


class Solution1:
    def numIdenticalPairs(self, nums: list[int]) -> int:

        counter = {}
        for el in nums:
            if el in counter:
                counter[el] += 1
            else:
                counter[el] = 1

        pairs = 0

        for _, val in counter.items():
            if val > 1:
                pairs += factorial(val) / (factorial(2) * factorial(val - 2))

        return int(pairs)


if __name__ == ('__main__'):
    print('sergey')
    nums = [1, 2, 3, 1, 1, 3, 1]
    print(Solution().numIdenticalPairs(nums))
    print(Solution1().numIdenticalPairs(nums))
    #rep5
