class SpaceVetor:
    def __init__(self, nums):
        self.lenght = len(nums)
        self.sparse_dict = {} #self.sparse_dict = {i:el for i,el in enumerate(nums)}
        for i, el in enumerate(nums):
                    if el:
                        self.sparse_dict[i] = el

    def dotProduct(self, vec): #self.sparse_dict.keys & vec.sparse_dict.keys()
        if self.lenght != vec.lenght:
            raise ValueError('Vectors should have equal length')

        s = 0
        for key in self.sparse_dict:
            if key in vec.sparse_dict:
                s += self.sparse_dict[key] * vec.sparse_dict[key]
        return s


if __name__ == '__main__':
    nums1 = [1,0,2,5]
    nums2 = [0,2,3,4]

    sv1 = SpaceVetor(nums1)
    sv2 = SpaceVetor(nums2)
    print(sv1.sparse_dict)
    print(sv2.sparse_dict)
    print(sv1.dotProduct(sv2))


#rep5+


