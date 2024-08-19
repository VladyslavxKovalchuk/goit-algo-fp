class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list.head

    def _sorted_insert(self, sorted_list, new_node):
        if sorted_list.head is None or sorted_list.head.data >= new_node.data:
            new_node.next = sorted_list.head
            sorted_list.head = new_node
        else:
            current = sorted_list.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def merge_sorted_lists(self, list1, list2):
        dummy = Node()
        tail = dummy
        head1 = list1.head
        head2 = list2.head

        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        tail.next = head1 if head1 else head2

        return LinkedList.from_head(dummy.next)

    @staticmethod
    def from_head(head):
        new_list = LinkedList()
        new_list.head = head
        return new_list
