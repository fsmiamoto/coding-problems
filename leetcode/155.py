class Node:
  def __init__(self, value, minimum = None, next = None):
    self.value = value
    self.next = next
    self.minimum = minimum

class MinStack:
    def __init__(self):
      self.head = None

    def push(self, val: int) -> None:
      if not self.head:
        # Empty stack, minimum value is val
        self.head = Node(val,val)
        return

      minimum = min(self.head.minimum,val)
      node = Node(val, minimum, self.head)
      self.head = node

    def pop(self) -> None:
      self.head = self.head.next

    def top(self) -> int:
      return self.head.value

    def getMin(self) -> int:
      return self.head.minimum
