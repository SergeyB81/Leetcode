class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)

        product = 1
        summ = 0
        for num in n_str:
            product = product * int(num)
            summ = summ + int(num)

        return product - summ