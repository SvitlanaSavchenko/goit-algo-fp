import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    # Ініціалізуємо словник для підрахунку кількості появ кожної суми
    sum_counts = {i: 0 for i in range(2, 13)}

    # Симуляція кидання кубиків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1

    # Обчислення ймовірностей
    probabilities = {k: v / num_rolls * 100 for k, v in sum_counts.items()}
    
    return sum_counts, probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.title('Ймовірність кожної суми при киданні двох кубиків')
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    num_rolls = 1000000  # Велика кількість кидків для точності
    sum_counts, probabilities = simulate_dice_rolls(num_rolls)
    
    # Виведення результатів
    print("Сума | Кількість появ | Ймовірність (%)")
    for sum_val in range(2, 13):
        print(f"{sum_val:<4} | {sum_counts[sum_val]:<15} | {probabilities[sum_val]:.2f}")
    
    # Побудова графіка
    plot_probabilities(probabilities)

if __name__ == "__main__":
    main()
