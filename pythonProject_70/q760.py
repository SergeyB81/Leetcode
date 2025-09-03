from typing import List

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = []

        # O(n**2)
        for el in nums1:
            mapping.append(nums2.index(el))
        return mapping


class Solution1:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping_d = {}
        # O(n)
        for i, el in enumerate(nums2):
            mapping_d[el] = i
        #return mapping_d

        # O(n)
        mapping = []
        for el in  nums1:
            mapping.append(mapping_d[el])
        return mapping




if __name__ == '__main__':
    print('sergey')
    nums1 = [12, 28, 46, 32, 50]
    nums2 = [50, 12, 32, 46, 28]
    print(Solution1().anagramMappings(nums1,nums2))

#rep5



