class Node:
  def __init__(self, val = None, next = None):
    self.val = val
    self.next = next

class LinkedList:
  def __init__(self, node = None):
    self.count = 0
    self.head = node
    self.tail = self.head
    if node:
      self.count = 1

  # append
  def append(self, val):
    # create a new node
    newNode = Node(val)

    if not self.head:
      self.head = newNode
      self.tail = self.head
    else:
      self.tail.next = newNode
      self.tail = self.tail.next
    self.count += 1

  # Insert a new node with val at given idx
  def insert(self, val, idx):
    pos = max(0, min(idx, self.count))
    newNode = Node(val)
    
    # Insert at head
    if pos == 0:
      newNode.next = self.head
      self.head = newNode
      if self.count == 0:
        self.tail = self.head
    # Insert at tail
    elif pos == self.count:
      self.tail.next = newNode
      self.tail = self.tail.next
    # Insert at middle
    else:
      curr = self.head
      count = 0
      while count < pos - 1:
        curr = curr.next
        count += 1
      newNode.next = curr.next
      curr.next = newNode
    self.count += 1

  # delete
  def delete(self, val):
    if not self.head:
      return None
    
    # Delete head
    # if self.head.val == val:
    #   self.head = self.head.next
    #   if not self.head: # List is now empty
    #     self.tail = None
    #   self.count -= 1
    #   return None
    
    sentinel = Node(-1)
    sentinel.next = self.head
    prev = sentinel
    curr = self.head

    while curr:
      if curr.val == val:
        # The sentinel node implicity set curr.next as the new head
        # if curr is head (it is more clear to explicitly set the new head)
        prev.next = curr.next
        if curr == self.tail: # Update tail if the deleted node was the tail
          self.tail = prev
        self.count -= 1 
        self.head = sentinel.next # Explicitly update head
        return None
      prev = curr
      curr = curr.next
    
    return None # Value not found

  def delete_head(self):
    if not self.head:
      return None
    
    oldHead = self.head
    self.head = self.head.next

    if self.head is None:
      self.tail = None
  
    self.count -= 1

    return oldHead
  
  def delete_tail(self):
    # zero node
    if not self.tail:
       return None

    oldTail = self.tail  
    # one node
    if self.head == self.tail:
      self.head = self.tail = None

    # more than one node
    else:
       curr = self.head
       while curr.next != self.tail:
          curr = curr.next
       self.tail = curr
       self.tail.next = None
    
    self.count -= 1
    return oldTail
      
  # find
  def find(self, val):
    curr = self.head

    while curr:
      if curr.val == val:
        return curr
      curr = curr.next

    return None
  
  def get_first_node(self):
    return self.head
  
  def get_last_node(self):
    return self.tail
   
  def reverse(self):
    if not self.head:
       return None
    
    prev = None
    curr = self.head

    # update tail
    self.tail = curr

    while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp

    # update head
    self.head = prev
    return self.head 
  
  def reverse_recurisve(self):
    def _reverse_recurisve(curr):
      if not curr or not curr.next:
        return curr 
      
      new_head = _reverse_recurisve(curr.next) # go until the last node is reached

      curr.next.next = curr
      curr.next = None
      
      return new_head 

    self.tail = self.head
    self.head = _reverse_recurisve(self.head)
     
# Test Cases 
import unittest

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_append(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.assertEqual(self.ll.get_first_node().val, 1)
        self.assertEqual(self.ll.get_last_node().val, 3)
        self.assertEqual(self.ll.count, 3)

    def test_insert(self):
        self.ll.append(1)
        self.ll.append(3)
        self.ll.insert(2, 1)
        self.assertEqual(self.ll.get_first_node().val, 1)
        self.assertEqual(self.ll.find(2).val, 2)
        self.assertEqual(self.ll.get_last_node().val, 3)
        self.assertEqual(self.ll.count, 3)
    
    def test_insert_at_head(self):
        self.ll.insert(1, 0)
        self.ll.insert(2, 0)
        self.ll.insert(3, 0)
        self.assertEqual(self.ll.get_first_node().val, 3)
        self.assertEqual(self.ll.get_last_node().val, 1)
        self.assertEqual(self.ll.count, 3)

    def test_insert_at_tail(self):
        self.ll.insert(1, 0)
        self.ll.insert(2, 1)
        self.ll.insert(3, 2)
        self.assertEqual(self.ll.get_first_node().val, 1)
        self.assertEqual(self.ll.get_last_node().val, 3)
        self.assertEqual(self.ll.count, 3)

    def test_delete(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.delete(2)
        self.assertIsNone(self.ll.find(2))
        self.assertEqual(self.ll.get_first_node().val, 1)
        self.assertEqual(self.ll.get_last_node().val, 3)
        self.assertEqual(self.ll.count, 2)

    def test_delete_head(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.delete_head()
        self.assertEqual(self.ll.get_first_node().val, 2)
        self.assertEqual(self.ll.count, 1)

    def test_delete_tail(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.delete_tail()
        self.assertEqual(self.ll.get_last_node().val, 1)
        self.assertEqual(self.ll.count, 1)

    def test_find(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.assertEqual(self.ll.find(2).val, 2)
        self.assertIsNone(self.ll.find(4))

    def test_reverse(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.reverse()
        self.assertEqual(self.ll.get_first_node().val, 3)
        self.assertEqual(self.ll.get_last_node().val, 1)
        self.assertEqual(self.ll.head.val, 3)
        self.assertEqual(self.ll.tail.val, 1)

    def test_reverse_single_node(self):
        self.ll.append(1)
        self.ll.reverse()
        self.assertEqual(self.ll.get_first_node().val, 1)
        self.assertEqual(self.ll.get_last_node().val, 1)
        self.assertEqual(self.ll.head.val, 1)
        self.assertEqual(self.ll.tail.val, 1)

    def test_reverse_recursive(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.reverse_recurisve()
        self.assertEqual(self.ll.get_first_node().val, 3)
        self.assertEqual(self.ll.get_last_node().val, 1)
        self.assertEqual(self.ll.head.val, 3)
        self.assertEqual(self.ll.tail.val, 1)

    def test_reverse_recurive_single_node(self):
        self.ll.append(1)
        self.ll.reverse_recurisve()
        self.assertEqual(self.ll.get_first_node().val, 1)
        self.assertEqual(self.ll.get_last_node().val, 1)
        self.assertEqual(self.ll.head.val, 1)
        self.assertEqual(self.ll.tail.val, 1)

    def test_reverse_empty_list(self):
        self.ll.reverse()
        self.assertIsNone(self.ll.get_first_node())
        self.assertIsNone(self.ll.get_last_node())

if __name__ == '__main__':
    unittest.main()