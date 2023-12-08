
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
    
    def append_list(self, list):
        for el in list:
            self.append(el)
    
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
        if (index >= self.length) or (index < 0):
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
    
    def remove(self, index):
        if (index < 0) or (index >= self.length):
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            target_node = self.head
            self.head = target_node.next
            target_node.next = None
        else:
            pre_target_node = self.get(index-1)
            target_node = pre_target_node.next
            pre_target_node.next = target_node.next
            target_node.next = None
            if index == self.length - 1:
                self.tail = pre_target_node
        
        self.length -= 1
        
    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        self.head, self.tail = self.tail, self.head
    
    def remove_duplicates(self):
        values = []
        previous = None
        current = self.head
        while current is not None:
            if current.value in values:
                previous.next = current.next
                current = current.next
            else:
                values.append(current.value)
                previous = current
                current = current.next
            
        
def merge_two_ordered_lists(l1, l2):
    pre_head = Node(-101)
    prev = pre_head
    
    while l2 and l1:
        if l1.value <= l2.value:
            prev.next = l1
            prev = prev.next
            l1 = l1.next
        else:
            prev.next = l2
            prev = prev.next
            l2 = l2.next
    
    if l1:
        prev.next = l1
    else:
        prev.next = l2
    
    return pre_head.next