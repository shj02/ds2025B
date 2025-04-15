class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)

    # 맨 앞에 추가하기
    def prepend(self, data):
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node