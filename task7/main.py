import random
import matplotlib.pyplot as plt

num_simulations = 100000

sums_count = {i: 0 for i in range(2, 13)}

for _ in range(num_simulations):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    sums_count[dice_sum] += 1

probabilities = {sum_: count / num_simulations for sum_, count in sums_count.items()}

print("Сума Ймовірність")
for sum_, prob in probabilities.items():
    print(f"{sum_}\t{prob:.4f}")

plt.bar(
    probabilities.keys(), probabilities.values(), tick_label=list(probabilities.keys())
)
plt.xlabel("Сума")
plt.ylabel("Ймовірність")
plt.title("Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)")
plt.show()
