# FILO - First In Last Out
# Implemented with list
class Stack:
  def __init__(self):
    self.length = 0
    self.stack = []

  def is_empty(self):
    return self.length == 0

  def push(self,val):
    self.stack.append(val)
    self.length += 1

  def pop(self):
    if self.is_empty():
      return None
    
    popped_elem = self.peek()
    self.stack = self.stack[:self.length-1]
    self.length -= 1
    return popped_elem
  
  def peek(self):
    if self.is_empty():
      return None
    
    return self.stack[self.length-1]

import unittest

class TestStack(unittest.TestCase):
  def setUp(self):
    self.st = Stack()

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
    self.assertEqual(self.st.length, 4)
    self.assertEqual(self.st.stack, [1,2,3,4])

  def test_pop(self):
    self.st.push(1)
    self.st.push(2)
    self.st.push(3)
    self.st.push(4)
    self.assertEqual(self.st.length, 4)
    self.st.pop()
    self.assertEqual(self.st.length, 3) 
    self.assertEqual(self.st.stack, [1,2,3])
    self.st.pop()
    self.assertEqual(self.st.length, 2) 
    self.assertEqual(self.st.stack, [1,2])

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
  
