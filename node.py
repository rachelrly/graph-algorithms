class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.visited = False

    def set_node_as_visited(self):
        self.visited = True
