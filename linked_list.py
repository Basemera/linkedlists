class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __len__(self):
        nodes = []
        for node in self:
            nodes.append(node.data)
        return len(nodes)

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.data)
        return " -> ".join(str(x) for x in nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            for node in self:
                pass
            node.next = new_node
        return self

    def insert_after(self, previous_node, new_node):
        if self.head is None:
            return "List is empty"
        for node in self:
            if node == previous_node:
                new_node.next = previous_node.next
                previous_node.next = new_node
                return self
        return "Node does not exist in list"

    def insert_before(self, next_node, new_node):
        if self.head == next_node:
            self.head = new_node
            new_node.next = next_node
        else:
            for node in self:
                if node == next_node:
                    previous_node.next = new_node
                    new_node.next = next_node
                    return self
                previous_node = node
        return "Node does not exist in list"


    def remove(self, new_node):
        previous_node = self.head
        for node in self:
            if node == new_node:
                previous_node.next = new_node.next
                return self
            previous_node = node
        return "Node does not exist in list"
