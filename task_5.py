import uuid
import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#FFFFFF"  # Колір за замовчуванням
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs_tree(root):
    if not root:
        raise ValueError("Root node is None")

    stack = [root]
    order = 0
    colors = {}
    while stack:
        node = stack.pop()
        if node:
            color = f"#{int(255 - (order * 255 / 10)):02X}0000"
            node.color = color
            colors[node.id] = color
            order += 1

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return colors

def bfs_tree(root):
    if not root:
        raise ValueError("Root node is None")

    queue = Queue()
    queue.put(root)
    order = 0
    colors = {}
    while not queue.empty():
        node = queue.get()
        if node:
            color = f"#{int(255 - (order * 255 / 10)):02X}0000"
            node.color = color
            colors[node.id] = color
            order += 1

            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
    return colors

def main():
    try:
        # Створення дерева
        root = Node(0)
        root.left = Node(4)
        root.left.left = Node(5)
        root.left.right = Node(10)
        root.right = Node(1)
        root.right.left = Node(3)

        # Обхід у глибину (DFS)
        print("DFS обход")
        dfs_colors = dfs_tree(root)
        draw_tree(root)

        # Обхід у ширину (BFS)
        print("BFS обход")
        bfs_colors = bfs_tree(root)
        draw_tree(root)

    except ValueError as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
