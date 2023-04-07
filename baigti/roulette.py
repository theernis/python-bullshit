length = int(input("length: "))

r_profit = 2
g_profit = 14
b_profit = 2

r_chance = 7
g_chance = 1
b_chance = 7

def test(r_cost, g_cost, b_cost):
    cost = (r_cost + g_cost + b_cost) * (r_chance + g_chance + b_chance)
    profit = r_cost * r_profit * r_chance + g_cost * g_profit * g_chance + b_cost * b_profit * b_chance
    return profit-cost

for r in range(length):
    for g in range(length):
        for b in range(length):
            profit = test(r+1, g+1, b+1)
            if True:
                print(f"r:{r+1},g:{g+1},b:{b+1},profit:{profit},profit per cost:{profit / (r+1 + g+1 + b+1)}")
print("end")
input()