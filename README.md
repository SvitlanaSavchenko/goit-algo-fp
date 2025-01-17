# Покрокова інструкція виконання фінального проєкту

## Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

- написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
- розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
- написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

## Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.

![Screenshoot](./res/image_1.png)

## Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

## Завдання 4. Візуалізація піраміди

Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.

```python
import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
def **init**(self, key, color="skyblue"):
self.left = None
self.right = None
self.val = key
self.color = color # Додатковий аргумент для зберігання кольору вузла
self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
if node is not None:
graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
if node.left:
graph.add_edge(node.id, node.left.id)
l = x - 1 / 2 ** layer
pos[node.left.id] = (l, y - 1)
l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
if node.right:
graph.add_edge(node.id, node.right.id)
r = x + 1 / 2 ** layer
pos[node.right.id] = (r, y - 1)
r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
return graph

def draw_tree(tree_root):
tree = nx.DiGraph()
pos = {tree_root.id: (0, 0)}
tree = add_edges(tree, tree_root, pos)

colors = [node[1]['color'] for node in tree.nodes(data=True)]
labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

plt.figure(figsize=(8, 5))
nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
plt.show()

# Створення дерева

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева

draw_tree(root)
```

![Screenshoot](./res/image_2.png)

Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.

> Примітка. Суть завдання полягає у створенні дерева із купи.

## Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад `#1296F0`). Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

> Примітка. Використовуйте стек та чергу, НЕ рекурсію

## Завдання 6. Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

```python
items = {
"pizza": {"cost": 50, "calories": 300},
"hamburger": {"cost": 40, "calories": 250},
"hot-dog": {"cost": 30, "calories": 200},
"pepsi": {"cost": 10, "calories": 100},
"cola": {"cost": 15, "calories": 220},
"potato": {"cost": 25, "calories": 350}
}
```

Розробіть функцію `greedy_algorithm` жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію `dynamic_programming`, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

## Завдання 7. Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

```Markdown
| Сума | Імовірність |
|------|-------------|
| 2    | 2.78% (1/36) |
| 3    | 5.56% (2/36) |
| 4    | 8.33% (3/36) |
| 5    | 11.11% (4/36) |
| 6    | 13.89% (5/36) |
| 7    | 16.67% (6/36) |
| 8    | 13.89% (5/36) |
| 9    | 11.11% (4/36) |
| 10   | 8.33% (3/36) |
| 11   | 5.56% (2/36) |
| 12   | 2.78% (1/36) |
```

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.

## Критерії прийняття фiнального проєкту

### Завдання 1:

- Реалізовано функцію реверсування однозв'язного списку, яка змінює посилання між вузлами. Код виконується.

- Програмно реалізовано алгоритм сортування (функцію) для однозв'язного списку. Код виконується.

- Реалізовано функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список. Код виконується.

### Завдання 2:

- Код виконується. Програма візуалізує фрактал “дерево Піфагора”.

- Користувач має можливість вказати рівень рекурсії.

### Завдання 3:

- Програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху у графі з використанням бінарної купи (піраміди).

- У межах реалізації завдання створено граф, використано піраміду для оптимізації вибору вершин та виконано обчислення найкоротших шляхів від початкової вершини до всіх інших.

### Завдання 4:

- Код виконується. Функція візуалізує бінарну купу.

### Завдання 5:

- Програмно реалізовано алгоритми DFS і BFS для візуалізації обходу дерева в глибину та в ширину. Використано стек та чергу.

- Кольори вузлів змінюються від темних до світлих відтінків залежно від порядку обходу.

### Завдання 6:

- Програмно реалізовано функцію, яка використовує принцип жадібного алгоритму. Код виконується і повертає назви страв, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

- Програмно реалізовано функцію, яка використовує принцип динамічного

програмування. Код виконується і повертає оптимальний набір страв для максимізації калорійності при заданому бюджеті.

### Завдання 7:

- Програмно реалізовано алгоритм для моделювання кидання двох ігрових кубиків і побудови таблиці сум та їх імовірностей за допомогою методу Монте-Карло.

- Код виконується та імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, підраховує, скільки разів кожна можлива сума з’являється у процесі симуляції, і визначає ймовірність кожної можливої суми.

- Створено таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

- Зроблено висновки щодо правильності розрахунків шляхом порівняння отриманих за допомогою методу Монте-Карло результатів та результатів аналітичних розрахунків. Висновки оформлено у вигляді файлу `readme.md` фінального завдання.

---

# Висновки по завданню

## Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

> ### Опис функцій
>
> #### `reverse(self)`
>
> Реверсує однозв'язний список, змінюючи посилання між вузлами. Використовуються три змінні:
>
> - **prev**: Зберігає попередній вузол.
> - **current**: Ітерується по списку.
> - **next_node**: Зберігає наступний вузол, щоб не втратити доступ до нього під час зміни посилань.
>
> #### `insertion_sort(self)`
>
> Сортує список методом вставки.
>
> - **sorted_head**: Утримує голову відсортованого часткового списку.
> - **\_sorted_insert**: Вставляє новий вузол у відсортований список у правильне місце.
>
> #### `merge_sorted_lists(head1, head2)`
>
> Зливає два відсортовані списки в один відсортований список. Використовує "допоміжний" вузол (`dummy`) для полегшення з'єднання вузлів.

```python
### Оригінальний список:

`1 -> 2 -> 3 -> None`

### Реверсований список:

`3 -> 2 -> 1 -> None`

### Несортований список:

`3 -> 1 -> 2 -> None`

### Відсортований список:

`1 -> 2 -> 3 -> None`

### Перший список:

`1 -> 3 -> 5 -> None`

### Другий список:

`2 -> 4 -> 6 -> None`

### Об'єднаний список:

`1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None`
```

## Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

> ### Функція `draw_tree`
>
> **Параметри:**
>
> - `branch_length`: довжина початкової гілки.
> - `angle`: кут між гілками.
> - `level`: рівень рекурсії.
> - `initial_thickness`: початкова товщина гілок.
>
> **Процес:**
>
> 1. Якщо рівень рекурсії менше або дорівнює нулю, функція завершується.
> 2. Малюється основна гілка за допомогою `turtle.forward(branch_length)`.
> 3. Рекурсивно малюються праві та ліві гілки:
>
> - Права гілка малюється після повороту на кут `angle`.
> - Ліва гілка малюється після повороту на `2 * angle` від початкової позиції.
>
> 4. Після малювання обох гілок черепашка повертається у вихідне положення за допомогою `turtle.right(angle)` та `turtle.backward(branch_length)`.
>
> ### Функція `main`
>
> **Процес:**
>
> 1. Запитує у користувача рівень рекурсії.
> 2. Перевіряє коректність введення (повинно бути невід'ємне ціле число).
> 3. Налаштовує екран `turtle` та початкову позицію черепашки:
>
> - Фон екрану встановлюється білим.
> - Черепашка розташована так, щоб дерево було видиме і вищим.
>
> 4. Викликає функцію `draw_tree` для малювання фрактала з заданими параметрами.
> 5. Завершує виконання малювання.
>
> ### Висновки
>
> - **Ефективність:** Рекурсивний підхід дозволяє легко малювати складні фрактальні структури. Розмір і товщина гілок можна налаштувати для досягнення бажаного вигляду.
> - **Читабельність:** Код добре структурований, що спрощує його розуміння та модифікацію. Функції мають чітко визначені завдання, що полегшує їх тестування та налагоджен

![Screenshoot](./res/task_2img.png)

## Завдання 3. Дерева, алгоритм Дейкстри

> ## Основи реалізації
>
> ### Клас `Graph`
>
> - **`__init__(self, vertices)`**:
> - Ініціалізує граф з певною кількістю вершин.
> - Створює список суміжності для зберігання ребер графа.
>
> - **`add_edge(self, u, v, w)`**:
> - Додає ребро з вагою `w` між вершинами `u` і `v`.
> - Для неорієнтованих графів додаються обидва напрями (від `u` до `v` і від `v` до `u`).
>
> ### Метод `dijkstra(self, start)`
>
> - **Ініціалізація**:
> - Ініціалізує масив відстаней до всіх вершин як нескінченність (`float('inf')`), крім початкової вершини (`start`), яка має відстань 0.
>
> - **Використання бінарної купи**:
> - Використовує модуль `heapq` для реалізації бінарної купи, що дозволяє ефективно вибирати вершину з найменшою відстанню.
>
> - **Оновлення відстаней**:
> - Для кожної вершини витягується мінімальна відстань і оновлюються відстані до сусідніх вершин, якщо знаходиться коротший шлях через поточну вершину.
>
> ### Функція `print_distances(distances)`
>
> - **Виведення відстаней**:
> - Виводить відстані до всіх вершин від початкової вершини.
>
> ### Функція `main()`
>
> - **Створення графа**:
> - Створює граф і додає до нього ребра за допомогою методу `add_edge`.
>
> - **Виконання алгоритму**:
> - Викликає алгоритм Дейкстри для визначення найкоротших шляхів від початкової вершини до всіх інших вершин.
>
> - **Виведення результатів**:
> - Виводить найкоротші відстані до всіх вершин від початкової вершини.

```python
Найкоротші шляхи від вершини 0
Відстань до вершини 0: 0
Відстань до вершини 1: 7
Відстань до вершини 2: 9
Відстань до вершини 3: 20
Відстань до вершини 4: 20
Відстань до вершини 5: 11
```

## Завдання 4. Візуалізація піраміди

> ### Висновки по реалізації
>
> 1. **`Node`**: Клас для створення вузлів бінарного дерева. Кожен вузол має:
>
>    - Унікальний ідентифікатор.
>    - Значення (`val`).
>    - Колір (`color`).
>    - Лівого і правого нащадків.
>
> 2. **`add_edges(graph, node, pos, x=0, y=0, layer=1)`**:
>
>    - Рекурсивно додає вузли та ребра до графа для візуалізації бінарного дерева.
>    - Встановлює позиції вузлів для побудови дерева на графіку.
>
> 3. **`visualize_tree(tree_root)`**:
>
>    - Візуалізує бінарне дерево за допомогою бібліотеки `networkx` для графів та `matplotlib` для малювання.
>    - Відображає вузли з їх кольорами та значеннями.
>
> 4. **`build_heap(arr)`**:
>
>    - Перетворює масив у бінарну купу (max-heap) за допомогою `heapify`.
>
> 5. **`heapify(arr, n, i)`**:
>
>    - Виправляє порушення властивостей купи для піддерева з коренем на позиції `i`.
>    - Використовується для перетворення масиву в купу.
>
> 6. **`convert_array_to_heap_tree(arr)`**:
>
>    - Конвертує масив у бінарне дерево, яке представляє купу.
>    - Створює вузли та встановлює їх лівих і правих нащадків відповідно до властивостей купи.
>
> 7. **`main()`**:
>    - Основна функція для створення дерева з масиву і його візуалізації.
>    - Викликає функції для перетворення масиву в дерево і його візуалізації.

## Завдання 5. Візуалізація обходу бінарного дерева

> ### Клас `Node`
>
> - **`__init__(self, key)`**: Ініціалізує вузол з унікальним ідентифікатором `id`, значенням `key` та кольором за замовчуванням (`#FFFFFF`).
>
> ### Функція `add_edges`
>
> - **`add_edges(graph, node, pos, x=0, y=0, layer=1)`**: Рекурсивно додає вузли і ребра до графа. Налаштовує позиції вузлів для відображення дерева.
>
> ### Функція `draw_tree`
>
> - **`draw_tree(tree_root)`**: Візуалізує дерево, використовуючи `networkx` та `matplotlib`. Відображає вузли з кольорами, визначеними в `dfs_tree` і `bfs_tree`.
>
> ### Функція `dfs_tree`
>
> - **`dfs_tree(root)`**: Реалізує обхід дерева в глибину (DFS) за допомогою стека. Призначає кожному вузлу унікальний колір в залежності від порядку обходу.
>
> ### Функція `bfs_tree`
>
> - **`bfs_tree(root)`**: Реалізує обхід дерева в ширину (BFS) за допомогою черги. Призначає кожному вузлу унікальний колір в залежності від порядку обходу.
>
> ### Функція `main`
>
> - **`main()`**: Створює бінарне дерево, виконує обхід у глибину та в ширину, і виводить результати. Включає обробку помилок для некоректних введень.

![Screenshoot](./res/task_5img.png)

## Завдання 6. Жадібні алгоритми та динамічне програмування

> ### Висновки по реалізації алгоритмів вибору їжі
>
> #### Жадібний алгоритм (`greedy_algorithm`):
>
> - **Принцип роботи**: Вибирає страви на основі максимального співвідношення калорій до вартості.
> - **Процес**: Страви сортуються за співвідношенням калорій до вартості у зменшувальному порядку, і потім вибираються страви, поки не буде досягнуто бюджет.
> - **Результат**: Виводить набір страв, що максимізує калорійність у межах заданого бюджету за жадібним підходом.
>
> #### Алгоритм динамічного програмування (`dynamic_programming`):
>
> - **Принцип роботи**: Використовує таблицю для обчислення максимальних калорій для кожного можливого бюджету.
> - **Процес**: Заповнює таблицю на основі вартості та калорійності кожної страви, потім визначає оптимальний набір страв для максимізації калорійності при заданому бюджеті.
> - **Результат**: Виводить оптимальний набір страв, що максимізує калорійність при заданому бюджеті, з урахуванням всіх можливих комбінацій.
>
> #### Обробка помилок:
>
> - **Перевірка**: Код враховує всі можливі випадки, забезпечуючи коректний вибір страв відповідно до бюджету.
>
> ### Висновок:
>
> Обидва алгоритми (жадібний та динамічного програмування) демонструють різні підходи до вирішення задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету. Жадібний алгоритм швидше працює, але може не завжди знаходити оптимальне рішення, тоді як алгоритм динамічного програмування забезпечує точний результат за рахунок більше часу виконання.

```python
Жадібний алгоритм:
Вибрані страви: ['cola', 'potato', 'pepsi', 'hot-dog']
Сумарна калорійність: 870
Алгоритм динамічного програмування:
Вибрані страви: ['potato', 'cola', 'pepsi', 'pizza']
Сумарна калорійність: 970
```

## Завдання 7. Використання методу Монте-Карло

> Програма була реалізована для симуляції великої кількості кидків двох ігрових кубиків. Ось основні етапи реалізації:
>
> 1. **Симуляція кидків**: Для кожного кидка визначалась сума чисел, які випали на двох кубиках, і підраховувалась кількість появ кожної можливої суми.
> 2. **Обчислення ймовірностей**: Ймовірності кожної суми були обчислені як відношення кількості появ до загальної кількості кидків, виражене у відсотках.
> 3. **Візуалізація**: Побудовано графік, що відображає ймовірності кожної суми.
>
> ### Висновок
>
> Результати симуляції методом Монте-Карло близькі до аналітичних розрахунків, що підтверджує коректність реалізації програми. Графік і таблиця надають візуальне уявлення про ймовірності кожної можливої суми при киданні двох кубиків, що дозволяє краще зрозуміти розподіл ймовірностей у таких випадках.

![Screenshoot](./res/task_7img.png)

```
Сума | Кількість появ | Ймовірність (%)
2    | 27864           | 2.79
3    | 55726           | 5.57
4    | 83279           | 8.33
5    | 111149          | 11.11
6    | 139106          | 13.91
7    | 166720          | 16.67
8    | 138554          | 13.86
9    | 110881          | 11.09
10   | 83265           | 8.33
11   | 55846           | 5.58
12   | 27610           | 2.76
```
