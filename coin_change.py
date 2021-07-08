def coin_change(coins, amount):
    def dp(n):
        if n == 0:
            return 0
        elif n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            sub_problem = dp(n - coin)
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        return res if res != float('INF') else -1

    return dp(amount)


coins = [2, 3]
amount = 8
res = coin_change(coins, amount)
print(res)
