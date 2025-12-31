### Overview
1. Linked Lists are not contiguous in memory like a list. Therefore, they have no indexes to access them.
2. They have **head** and **tail** variables.
3. The node is both the value and the pointer; you can think of it as a nested dictionary.

Another representation of a Linked List: 

<img width="765" height="444" alt="image" src="https://github.com/user-attachments/assets/8865b59f-0ec6-4f06-8f86-36b62cf357ab" />

### Big-O
1. Append a new node at the end - `O(1)`
   1. It doesn’t matter how many nodes we have on the list. The number of operations to add in the end is exactly the same.
2. Remove a tail - `O(n)`
   1. Iterate through the entire linked list to find the pointer of the last node, then set the tail to the last node.
3. Adding a node to the front - `O(1)`
   1. Same reason for the first scenario.
4. Removing the first node - `O(1)`
   1. Repointing the head variable to the next node. The size of the linked list doesn’t matter.
5. Inserting a node in the middle - `O(n)`
   1. Iterating through the linked list to distinguish the precedent node, then connect the new node to the antecedent node, and finally connect the precedent to the new node.
6. Removing a node in the middle - `O(n)`
   1. Iterating through the linked list to find the node to be removed. Then update the pointers accordingly.
7. Finding a node - `O(n)`
   1. Iterating through the linked list to find the node.

### Constructors
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```
```python
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


my_linked_list = LinkedList(11)
```

### LL Functions
#### Print
```python
def print_list(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next


my_linked_list.print_list()
```
#### Append
```python
def append(self, value):
    new_node = Node(value)
    if self.length == 0:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
    self.length += 1
    return True


my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
```
#### Pop
```python
def pop(self):
    if self.length == 0: # edge case where it’s empty
        return None

    pre = self.head 
    temp = self.head

    while (temp.next):
        pre = temp
        temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1

    if self.length == 0: # edge case where you only have one item
        self.head = None
        self.tail = None
    
    return temp.value

my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop())
# (1) Item -Returns 1 Node
print(my_linked_list.pop())
# (0) Items -Returns None
print(my_linked_list.pop())
```
#### Prepend
```python
def prepend(self, value):
    new_node = Node(value)

    if self.length == 0:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head = new_node
   
    self.length += 1
   
    return True

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.prepend(0)
```
#### Pop First
```python
def pop_first(self):
    if self.length == 0: # edge case where it’s empty
        return None
    
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1

    if self.length == 0:
        self.tail == None

    return temp.value
```
#### Get
```python
def get(self, index):
    if index < 0 or index > self.length:
        return None
    temp = self.head

    for _ in range(index):
        temp = temp.next
    return temp.value
```
#### Set
```python
def set(self, index, value):
    if index < 0 or index > self.length:
        return None
    temp = self.head

    for _ in range(index):
        temp = temp.next
    return temp.value
```
#### Insert
```python
def insert(self, index, value):
    if index < 0 or index > self.length:
        return False
    
    if index == 0:
        return self.prepend(value)
    
    if self.length == index:
        self.append(value)

    new_node = Node(value)
    temp = self.get(index-1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True
```
