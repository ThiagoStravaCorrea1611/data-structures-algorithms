

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '-->'
            temp_node = temp_node.next
        
        return result
    
    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index >= self.length - 1:
            self.append(value)
        else:
            new_node = Node(value)
            temp_node = self.head
            for i in range(index-1):
                temp_node = temp_node.next
        
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return (True, index)
            current = current.next
            index += 1
        
        return (False, None)
    
    def get(self, index):
        if index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current
    
    def set_value(self, index, value):
        target_node = self.get(index)
        if target_node is not None:
            target_node.value = value
            return True
        return False
    
    def pop_first(self):
        target_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = target_node.next
            target_node.next = None
        self.length -= 1
        return target_node
    
    def pop_last(self):
        target_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.get(self.length - 2)
            self.tail.next = None
        self.length -= 1
        return target_node
        

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(70)
new_linked_list.prepend(40)
new_linked_list.insert(0, "vlublu")
new_linked_list.insert(99, "vlribvlruba")
new_linked_list.insert(2, 42)
new_linked_list.insert(4, 69)
print(new_linked_list.length)
print(new_linked_list)
new_linked_list.traverse()
print(new_linked_list.search(70))
print(new_linked_list.search("vlublu"))
print(new_linked_list.search(20))
print(new_linked_list.search("vlribvlruba"))
print(new_linked_list.search("fake"))
print(new_linked_list.search(123123))
print(new_linked_list.get(3))
print(new_linked_list.get(0))
print(new_linked_list.get(99))
print(new_linked_list.get(8))
print(new_linked_list.get(7))
print(new_linked_list.set_value(0, 0))
print(new_linked_list.set_value(7, 9999))
print(new_linked_list.set_value(43, 43))
print(new_linked_list)
print(new_linked_list.pop_first())
print(new_linked_list)
print(new_linked_list.pop_last())
print(new_linked_list.pop_last())
print(new_linked_list)
test_linked_list = LinkedList()
test_linked_list.append(10)
print(test_linked_list)
print(test_linked_list.pop_first())
print(test_linked_list)
print(test_linked_list.pop_first())
print(test_linked_list)
test_linked_list = LinkedList()
test_linked_list.append(10)
test_linked_list.append(20)
print(test_linked_list)
print(test_linked_list.pop_last())
print(test_linked_list)
print(test_linked_list.pop_last())
print(test_linked_list.pop_last())
print(test_linked_list)