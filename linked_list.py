

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
