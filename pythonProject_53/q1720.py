'''
XOR (⊕) — это битовая операция, которая сравнивает соответствующие
 биты двух чисел и возвращает 1, если биты различаются, и 0,
  если они одинаковы.
Операция XOR в Python выполняется с помощью оператора `^`
a = 5    В бинарном виде: 0101
b = 3    В бинарном виде: 0011
result = a ^ b  # 0101 ⊕ 0011 = 0110 (6 в десятичной системе)
'''

class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        """
        Декодирует массив, закодированный с помощью XOR.

        Параметры:
            encoded (list[int]): Закодированный массив (encoded[i] = arr[i] XOR arr[i+1]).
            first (int): Первый элемент исходного массива (arr[0]).

        Возвращает:
            list[int]: Декодированный массив.
        """
        decoded = [first]  # Начинаем с первого известного элемента

        for i in range(len(encoded)):
            # Каждый следующий элемент вычисляется как XOR текущего encoded[i] и предыдущего decoded[i]
            # Поскольку encoded[i] = decoded[i] ⊕ decoded[i+1],
            # то decoded[i+1] = encoded[i] ⊕ decoded[i]
            next_element = encoded[i] ^ decoded[i]
            decoded.append(next_element)

        return decoded


if __name__ == '__main__':
    # Пример использования
    encoded = [6, 2, 7, 3]  # Закодированные данные
    first = 5  # Первый элемент исходного массива

    # Декодируем и выводим результат
    print(Solution().decode(encoded, first))  # Ожидаемый вывод: [5, 3, 1, 4, 7]