class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0          # указатель для проверки элементов
        n = len(nums)  # текущая "живая" длина массива
        while i < n:
            if nums[i] == val:
                # заменяем удаляемый элемент на последний
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1   # переходим к следующему
        return nums, n  # возвращаем новую длину


if __name__ == ('__main__'):
    print('Sergey')

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(Solution().removeElement(nums, val))