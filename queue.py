from node import Node

class Queue:
    def __init__(self, first_node, last_node):
        self.first_node = None
        self.last_node = None

    def enqueue(self, value):
        node = Node(value)

        if self.first_node == None:
          self.first_node = node

        if self.last_node != None:
          self.last_node.next = node

        self.last_node = node

    def dequeue(self):
      if self.first_node == None: return
      node = self.first_node
      self.first_node = self.first_node.next

      if node == self.last_node:
        self.last_node = None

      return node.value