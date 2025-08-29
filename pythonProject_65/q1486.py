class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = start
        for i in range(1, n):
            xor = xor ^ (start + i * 2)
        return xor
""" Вычисляет XOR последовательности чисел, генерируемой по формуле: nums[i] = start + 2*i
   XOR (исключающее ИЛИ) - битовая операция, которая возвращает:
   - 1 если биты разные
   - 0 если биты одинаковые
   Правила XOR:
   0 ^ 0 = 0
   0 ^ 1 = 1
   1 ^ 0 = 1
   1 ^ 1 = 0
   Свойства XOR:
   - Коммутативность: a ^ b = b ^ a
   - Ассоциативность: (a ^ b) ^ c = a ^ (b ^ c)
   - a ^ a = 0 (самообратимость)
   - a ^ 0 = a (нейтральный элемент)
   Название: Exclusive OR (исключающее ИЛИ)
   """
if __name__ == ('__main__'):
    print('sergey')
    n = 4
    start = 3
    print(Solution().xorOperation(n, start))

 #rep5
