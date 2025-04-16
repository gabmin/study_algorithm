class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return

    def pop(self):
        if self.is_empty():
            return print("stack is empty")
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return print("stack is empty")
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None