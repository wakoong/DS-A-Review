# LIFO - Last In First Out
# Implemented with linked list

from LinkedList import LinkedList

class StackV2:
  def __init__(self):
    self.stack = LinkedList()

  # isEmpty
  def is_empty(self):
    return self.stack.count == 0
  
  def peek(self):
    if self.is_empty():
      return None
    
    return self.stack.get_first_node().val

  def push(self, val):
    self.stack.insert(val,0)

  def pop(self):
    if self.is_empty():
      return None
    
    # head is the top of the stack
    # and tail is the bottom of the stack
    popped_elem = self.stack.delete_head() 
    return popped_elem

  def to_array(self):
    result = []
    curr = self.stack.head
    while curr:
      result.append(curr.val)
      curr = curr.next

    return result

import unittest

class TestStack(unittest.TestCase):
  def setUp(self):
    self.st = StackV2()

  def test_is_empty(self):
    self.assertEqual(self.st.is_empty(), True)
    self.st.push(1)
    self.assertEqual(self.st.is_empty(), False)
    self.st.pop()
    self.assertEqual(self.st.is_empty(), True)

  def test_push(self):
    self.st.push(1)
    self.st.push(2)
    self.st.push(3)
    self.st.push(4)
    self.assertEqual(self.st.stack.count, 4)
    self.assertEqual(self.st.to_array(), [4,3,2,1])

  def test_pop(self):
    self.st.push(1)
    self.st.push(2)
    self.st.push(3)
    self.st.push(4)
    self.assertEqual(self.st.stack.count, 4)
    self.st.pop()
    self.assertEqual(self.st.stack.count, 3) 
    self.assertEqual(self.st.to_array(), [3,2,1])
    self.st.pop()
    self.assertEqual(self.st.stack.count, 2) 
    self.assertEqual(self.st.to_array(), [2,1])

  def test_peek(self):
    self.st.push(1)
    self.st.push(2)
    self.st.push(3)
    self.st.push(4)
    self.assertEqual(self.st.peek(), 4)  
    self.st.pop()
    self.assertEqual(self.st.peek(), 3)

if __name__ == '__main__':
    unittest.main()