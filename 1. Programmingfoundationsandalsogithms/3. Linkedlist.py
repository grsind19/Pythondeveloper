# LinkedList example

class Node(object):
  def __init__(self,val):
    self.val = val
    self.next = None
  def get_data(self):
    return self.val
  
  def set_data(self,val):
    self.val = val
  
  def get_next(self):
    return self.next

  def set_next(self, next):
    self.next = next

class LinkedList(object):
  def __init__(self, head = None):
    self.count = 0
    self.head = head
  
  def insert(self,data):
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head= new_node
    self.count +=1
  
  def find(self, val):
    item = self.head
    while(item !=None):
      if item.get_data()==val:
        return item
      else:
        item = item.get_next()
    
    return None
  
  def delete(self, idx):
    if idx > self.count -1:
      return
    if idx == 0:
      self.head  = self.head.get_next()
    else:
      tempIdx =0
      node = self.head
      while tempIdx < idx -1:
        node = node.get_next()
        tempIdx+=1
      node.set_next(node.get_next().get_next())
      self.count -=1
      
      




itemList = LinkedList()

itemList.insert(10)
itemList.insert(20)

print(itemList.find(10).val)
print(itemList.find(30))
itemList.delete(1)
print(itemList.find(10))
print(itemList.count)
