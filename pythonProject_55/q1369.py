class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []
        n = len(nums)
        # O(n**2)
        for i in range(n):
            target.insert(index[i], nums[i])
        return target


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    print(Solution().createTargetArray(nums, index))

    # rep 5