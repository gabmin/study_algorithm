# [5] -> [12] -> [8]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # 제일 마지막 노드에 새로운 노드 추가
    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # 모든 링크드 리스트 출력
    def print_all(self):
        cur = self.head

        while cur is not None:
            print(cur.data)
            cur = cur.next

    # index 번째의 노드 가져오기
    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

    # index 번재에 value 추가
    def add_node(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.get_node(index - 1)
            next_node = prev_node.next
            prev_node.next = new_node
            new_node.next = next_node

    # index 번째 node 삭제
    def delete_node(self, index):

        if(index == 0):
            self.head = self.head.next
        else:
            prev_node = self.get_node(index - 1)
            index_node = self.get_node(index)

            prev_node.next = index_node.next



linked_list = LinkedList(5)

linked_list.append(12)
linked_list.append(8)

linked_list.add_node(0, 9)

linked_list.delete_node(0)
linked_list.print_all()
