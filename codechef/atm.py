# https://www.codechef.com/problems/HS08TEST

amount, balance = input().split()
amount = int(amount)
balance = float(balance)

if amount > balance - 0.50:
    print(balance)
elif amount % 5 != 0:
    print(balance)
else:
    print(balance - amount - 0.50)
