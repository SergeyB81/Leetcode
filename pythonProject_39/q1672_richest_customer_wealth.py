from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []

        for account in accounts:
            s = 0
            for bank in account:
                s = s + bank
            wealth.append(s)
        print(wealth)

        cur_max = wealth[0]
        for w in wealth[1:]:
            if w > cur_max:
                cur_max = w

        return print(cur_max)


if __name__ == '__main__':

    accounts = [[1,5],[7,3],[3,5]]

    Solution().maximumWealth(accounts)

    def maximum_wealth(accounts):
        # return max(map(sum,accounts))
        return max([sum(acc) for acc in accounts])

    print(maximum_wealth(accounts))


    def maximum_wealth_ef(accounts):
        cur_max = float('-inf')
        for account in accounts:
            s = 0
            for bank in account:
                s = s + bank

            if s > cur_max:
                cur_max = s

        return cur_max


    print(maximum_wealth_ef(accounts))

    #rep5


