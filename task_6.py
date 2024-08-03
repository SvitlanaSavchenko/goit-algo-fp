# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    # Сортування страв за співвідношенням калорій до вартості у зменшувальному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            chosen_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return chosen_items, total_calories

def dynamic_programming(budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[name]['cost'] for name in item_names]
    calories = [items[name]['calories'] for name in item_names]

    # Ініціалізація таблиці для динамічного програмування
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнення таблиці
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Визначення оптимального набору страв
    w = budget
    chosen_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(item_names[i - 1])
            w -= costs[i - 1]
    
    return chosen_items, dp[n][budget]

def main():
    budget = 100  # Встановіть свій бюджет

    # Виконання жадібного алгоритму
    greedy_items, greedy_calories = greedy_algorithm(budget)
    print("Жадібний алгоритм:")
    print("Вибрані страви:", greedy_items)
    print("Сумарна калорійність:", greedy_calories)

    # Виконання алгоритму динамічного програмування
    dp_items, dp_calories = dynamic_programming(budget)
    print("Алгоритм динамічного програмування:")
    print("Вибрані страви:", dp_items)
    print("Сумарна калорійність:", dp_calories)

if __name__ == "__main__":
    main()
