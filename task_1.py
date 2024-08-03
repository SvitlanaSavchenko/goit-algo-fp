class Node:
    """Клас для представлення вузла однозв'язного списку."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Клас для представлення однозв'язного списку."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Додає новий вузол в кінець списку."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def print_list(self):
        """Виводить елементи списку."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Реверсує однозв'язний список."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        """Сортує список методом вставки."""
        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node
        self.head = sorted_head

    def _sorted_insert(self, sorted_head, node):
        """Вставляє вузол в відсортований список."""
        if not sorted_head or sorted_head.data >= node.data:
            node.next = sorted_head
            return node
        current = sorted_head
        while current.next and current.next.data < node.data:
            current = current.next
        node.next = current.next
        current.next = node
        return sorted_head

    @staticmethod
    def merge_sorted_lists(head1, head2):
        """Об'єднує два відсортовані списки."""
        dummy = Node(0)
        tail = dummy
        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        tail.next = head1 or head2
        return dummy.next

def main():
    """Основна функція для тестування списків."""
    # Тестування реверсування списку
    ll = LinkedList()
    for value in [1, 2, 3]:
        ll.append(value)
    print("Оригінальний список:")
    ll.print_list()

    ll.reverse()
    print("Реверсований список:")
    ll.print_list()

    # Тестування сортування
    ll = LinkedList()
    for value in [3, 1, 2]:
        ll.append(value)
    print("Несортований список:")
    ll.print_list()

    ll.insertion_sort()
    print("Відсортований список:")
    ll.print_list()

    # Тестування об'єднання
    ll1 = LinkedList()
    for value in [1, 3, 5]:
        ll1.append(value)

    ll2 = LinkedList()
    for value in [2, 4, 6]:
        ll2.append(value)

    print("Перший список:")
    ll1.print_list()
    print("Другий список:")
    ll2.print_list()

    merged_head = LinkedList.merge_sorted_lists(ll1.head, ll2.head)
    print("Об'єднаний список:")
    merged_list = LinkedList()
    merged_list.head = merged_head
    merged_list.print_list()

if __name__ == "__main__":
    main()
