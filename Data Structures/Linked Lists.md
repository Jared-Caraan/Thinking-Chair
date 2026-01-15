### Overview
1. Linked Lists are not contiguous in memory like a list. Therefore, they have no indexes to access them.
2. They have **head** and **tail** variables.
3. The node is both the value and the pointer; you can think of it as a nested dictionary.

Another representation of a Linked List: 

<img width="765" height="444" alt="image" src="https://github.com/user-attachments/assets/8865b59f-0ec6-4f06-8f86-36b62cf357ab" />

##

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

##

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

##

## LL Functions
### Print List
#### Code
```python
def print_list(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next


my_linked_list.print_list()
```
#### Visual
![print](https://github.com/user-attachments/assets/89865c91-f3fc-425d-9e11-c6829f38f5c4)


##

#### Append

**Intuition (one or more items)**
1. Create a new node.
2. We'll have that last item on that list point at the new node.
3. Then we have the `tail` point at the new node.
4. Increase the size of the LL.

**Edge Case**
1. We don't have any items.
      1. In this case, we want both `head` and `tail` point at the new node.

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

##

#### Pop

**Intuition (two or more items)**
1. Create two variables, both pointing at the `head`.
2. Loop forward until one variable is at the `tail`, and another one is at the node before the `tail`.
3. Return the variable that's on the `tail` and detach it.
4. Make the other variable the `tail`.
5. Decrease the size of the LL.

**Edge Cases**
1. We don't have any items.
      1. Return `None` 
2. We have only one node.
      2. After detaching the tail, point both `head` and `tail` to `None`.

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
    
    return temp

my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop())
# (1) Item -Returns 1 Node
print(my_linked_list.pop())
# (0) Items -Returns None
print(my_linked_list.pop())
```

##

#### Prepend

**Intuition (two or more items)**
1. Point the new node at the current `head` of the LL.
2. Set the `head` to the new node.
3. Increment the length of the LL.

**Edge Cases**
1. We don't have any items.
      1. Point the `head` and `tail` to the new node.

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

##

#### Pop First

**Intuition (two or more items)**
1. Point `temp` to the current `head`.
2. Move the `head` to the next node.
3. Detach `temp` from the rest of the LL.
4. Decrement the length of the LL.
5. Return the node.

**Edge Cases**
1. We don't have any items.
      1. Return `None`.
2. We have one item.
      2. After step 4, just add the condition to point the `tail` to `None`.

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

    return temp
```

##

#### Get

**Intuition (two or more items)**
1. Point `temp` to the current `head`.
2. Iterate through the LL a number of times equal to the index specified

**Edge Cases**
1. Invalid index.
      1. Return `None`.

```python
def get(self, index):
    if index < 0 or index > self.length:
        return None
    temp = self.head

    for _ in range(index):
        temp = temp.next
    return temp
```

##

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

##

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
