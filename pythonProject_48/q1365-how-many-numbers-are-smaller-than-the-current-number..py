class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        nums_sorted = sorted(nums) # n log n
        #print(nums_sorted)

        for i, el in enumerate(nums): # n
            nums[i] = nums_sorted.index(el)
        return nums


if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3, 7, 9]
    print(Solution().smallerNumbersThanCurrent(nums))
    #rep5+