
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
            self.tail.next = self.head
        
        self.length += 1
    
    def __str__(self):
        temp_node = self.head
        if self.length == 1:
            return str(self.head.value)
        
        result = ''
        while temp_node.next != self.head:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '-->'
            temp_node = temp_node.next
        
        return result

test_circular_linked_list = CircularLinkedList()
test_circular_linked_list.append(1)
print(test_circular_linked_list)
test_circular_linked_list.append_list([10, 20, 30, 40, 50])
print(test_circular_linked_list)
test_circular_linked_list.prepend(99)
print(test_circular_linked_list)