from typing import List


# brute force O(n**2)
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0  # если меньше 2 цен — не получится купить и продать

        n = len(prices)
        deals = []  # список всех возможных прибылей
        for i in range(n):
            for j in range(i + 1, n):  # ищем максимум только после покупки
                deals.append(prices[j] - prices[i])  # прибыль: продал - купил

        # возвращаем максимальную прибыль или 0, если все отрицательные
        return max(max(deals), 0)



class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        n = len(prices)
        i = 0  # индекс покупки
        j = 1  # индекс продажи
        cur_max = prices[j] - prices[i]  # начальная прибыль

        while i < j < n and i < n:
            if prices[j] <= prices[i]:
                # если продажа невыгодна или убыточна — смещаем оба указателя
                j += 1
                i += 1
            else:
                # прибыль возможна
                cur = prices[j] - prices[i]
                if cur > cur_max:
                    cur_max = cur  # обновляем максимум
                j += 1  # пробуем продать позже

        return cur_max


class Solution3:
    def maxProfit(self, prices):
        max_profit = 0
        min_price = float('inf')  # инициализируем бесконечным минимумом

        for price in prices:
            # на каждом шаге обновляем минимальную цену
            min_price = min(min_price, price)

            # считаем потенциальную прибыль, если продать сегодня
            profit = price - min_price

            # обновляем максимум прибыли
            max_profit = max(max_profit, profit)

        return max_profit

if __name__ == '__main__':
    prices = [7, 3, 15 ,5, 1, 8, 12, 4]
    print(Solution3().maxProfit(prices))

    # rep5
