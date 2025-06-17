class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for el in nums:
            ans.append(nums[el])
        return ans


class Solution1:
    def buildArray1(self, nums: list[int]) -> list[int]:
        return list(map(nums.__getitem__, nums))




if __name__ == "__main__":
    nums = [0, 2, 1, 5, 3, 4]
    print(Solution().buildArray(nums))
    print('hello')


    # rep5
