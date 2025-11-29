class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)

        product = 1
        summ = 0
        for num in n_str:
            product = product * int(num)
            summ = summ + int(num)

        return product - summ


    def subtractProductAndSum1(self, n: int) -> int:
        # Инициализируем переменные:
        product = 1  # Для хранения произведения цифр числа n
        summ = 0  # Для хранения суммы цифр числа n
        mult = 0  # Счетчик степени десятки для извлечения цифр

        # Цикл продолжается, пока результат деления n на 10^mult не равен нулю
        while n // 10 ** mult:
            # Извлекаем текущую цифру по разряду:
            # Сначала берем остаток от деления на 10^(mult+1), чтобы "отрезать" старшие цифры
            # Затем делим на 10^mult, чтобы получить нужную цифру
            digit = (n % 10 ** (mult + 1)) // 10 ** mult

            # Умножаем текущую цифру на произведение
            product = product * digit

            # Прибавляем текущую цифру к сумме
            summ = summ + digit

            # Увеличиваем счетчик степени для перехода к следующей цифре
            mult = mult + 1



        return product - summ

    def subtractProductAndSum2(self, n: int) -> int:

        product = 1
        summ = 0
        while n > 0:
            digit = n % 10  # Последняя цифра
            product *= digit
            summ += digit
            n //= 10  # Удаляем последнюю цифру

        return product - summ




if __name__ == '__main__':
    n = 238
    print(Solution().subtractProductAndSum1(n))

    # rep 5