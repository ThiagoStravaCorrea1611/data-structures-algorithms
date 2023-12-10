
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        
        self.length += 1
    
    def append_list(self, list):
        for el in list:
            self.append(el)
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        
        self.length += 1
    
    def __str__(self):
        temp_node = self.head
        if self.length == 0:
            return ''
        
        result = ''
        while temp_node:
            result += str(temp_node.value)
            result += '-->'
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        
        return result
    
    def insert(self, index, value):
        if index < 0:
            return None
        elif (self.length == 0) or (index >= self.length-1):
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(index-1):
                current = current.next
            displaced_node = current.next
            current.next = new_node
            new_node.next = displaced_node

test_circular_linked_list = CircularLinkedList()
print(test_circular_linked_list)
test_circular_linked_list.append(1)
print(test_circular_linked_list)
test_circular_linked_list.append_list([10, 20, 30, 40, 50])
print(test_circular_linked_list)
test_circular_linked_list.prepend(99)
print(test_circular_linked_list)
test_circular_linked_list.insert(0, "vlubavluba")
test_circular_linked_list.insert(99, "varabuba")
test_circular_linked_list.insert(5, "hurashuha")
print(test_circular_linked_list)
print(test_circular_linked_list.head.value)
print(test_circular_linked_list.tail.value)
print(test_circular_linked_list.tail.next.value)