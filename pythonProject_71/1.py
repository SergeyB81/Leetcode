class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        d= {}

        for i in range(n):
            compliment = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            else: d[compliment] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
