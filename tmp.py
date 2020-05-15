def withdraw(amount):
    print(amount)

    # for 100 bills
    bills_100 = amount // 100
    remaind_100 = amount % 100
    if (remaind_100 == 30 or remaind_100 == 10):
        bills_100 -= 1
    amount -= bills_100 * 100

    # 50 might be only one
    if amount % 20 == 0 or amount < 50:
        bills_50 = 0
    else:
        bills_50 = 1
    amount -= bills_50 * 50

    bills_20 = amount // 20

    print([bills_100, bills_50, bills_20])
    return [bills_100, bills_50, bills_20]

print(floor(10 / 2))
