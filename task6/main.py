def greedy_dish_selection(dishes, budget):
    dishes.sort(key=lambda x: x[1] / x[2], reverse=True)

    selected_dishes = []
    total_cost = 0
    total_calories = 0

    for dish in dishes:
        name, calories, cost = dish
        if total_cost + cost <= budget:
            selected_dishes.append(name)
            total_cost += cost
            total_calories += calories

    return selected_dishes, total_cost


def dynamic_dish_selection(dishes, budget):
    n = len(dishes)
    dp = [0] * (budget + 1)
    item_keep = [[0] * (budget + 1) for _ in range(n)]

    for i in range(n):
        name, calories, cost = dishes[i]
        for j in range(budget, cost - 1, -1):
            if dp[j] < dp[j - cost] + calories:
                dp[j] = dp[j - cost] + calories
                item_keep[i][j] = 1

    selected_dishes = []
    total_cost = 0
    w = budget

    for i in range(n - 1, -1, -1):
        if item_keep[i][w]:
            name, calories, cost = dishes[i]
            selected_dishes.append(name)
            w -= cost
            total_cost += cost

    return selected_dishes, total_cost


dishes = [("Salad", 200, 5), ("Pizza", 500, 20), ("Soup", 150, 7), ("Pasta", 350, 15)]
budget = int(input("Введіть бюджет: "))


print("Жадібний алгоритм")
print(greedy_dish_selection(dishes, budget))
print()
print("Динамічне програмування")
print(dynamic_dish_selection(dishes, budget))
