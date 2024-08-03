import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v, w):
        """Додає ребро з вагою w між вершинами u і v."""
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))  # Для неорієнтованого графа
    
    def dijkstra(self, start):
        """Виконує алгоритм Дейкстри для знаходження найкоротших шляхів від вершини start."""
        distances = [float('inf')] * self.V
        distances[start] = 0
        min_heap = [(0, start)]  # (відстань, вершина)
        
        while min_heap:
            current_distance, u = heapq.heappop(min_heap)
            
            if current_distance > distances[u]:
                continue
            
            for v, weight in self.adj_list[u]:
                distance = current_distance + weight
                
                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(min_heap, (distance, v))
        
        return distances

def print_distances(distances):
    """Виводить відстані до всіх вершин від початкової вершини."""
    for i, dist in enumerate(distances):
        print(f"Відстань до вершини {i}: {dist}")

def main():
    # Кількість вершин у графі
    V = 6
    
    # Створення графа
    graph = Graph(V)
    
    # Додавання ребер до графа
    graph.add_edge(0, 1, 7)
    graph.add_edge(0, 2, 9)
    graph.add_edge(0, 5, 14)
    graph.add_edge(1, 2, 10)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 11)
    graph.add_edge(2, 5, 2)
    graph.add_edge(3, 4, 6)
    graph.add_edge(4, 5, 9)
    
    # Визначення початкової вершини
    start_vertex = 0
    
    # Виконання алгоритму Дейкстри
    distances = graph.dijkstra(start_vertex)
    
    # Виведення результатів
    print("Найкоротші шляхи від вершини", start_vertex)
    print_distances(distances)

if __name__ == "__main__":
    main()
