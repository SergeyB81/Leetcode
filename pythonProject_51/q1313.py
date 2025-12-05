class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        """
                Декомпрессия списка, сжатого методом Run-Length Encoding (RLE).
                Входной список представляет собой пары [частота, значение].
                Функция возвращает декомпрессированный список, где каждое значение
                повторяется указанное количество раз.
        """
        n = len(nums)
        answer = []
        for i in range(0, n, 2):
            answer += nums[i] * [nums[i + 1]]
        return answer

if __name__ == ('__main__'):

        nums = [1,2,3,4]
        print(Solution().decompressRLElist(nums))

# rep+

