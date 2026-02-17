class Solution:
    def anagramMappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        mapping = []

        for el in nums1:
            mapping.append(nums2.index(el))
        return mapping

    def anagramMappings1(self, nums1: list[int], nums2: list[int]) -> list[int]:
        mapping_d = {}

        for i, el in enumerate(nums2):
            mapping_d[el] = i

        mapping = []
        for el in nums1:
            mapping.append(mapping_d[el])
        return mapping



if __name__ == '__main__':
    nums1 = [12, 28, 46, 32, 50]
    nums2 = [50, 12, 32, 46, 28]
    print(Solution().anagramMappings1(nums1, nums2))
