# Creating a Node:-
class Node(object):
    def __init__(self, data):
        self.data = data
        self.NextNode = None  # NextNode = NEXT NODE REFERENCE...
        self.PrevNode = None  # PrevNode = PREVIOUS NODE REFERENCE...
        
        
        
# Creating a Doubly Linked List:-
class Doubly(object):
    def __init__(self):
        self.head = None  # First Node is Empty...
        
        
     
    # Traversing elements in the forward direction:-
    def traverse_forward(self):
        if self.head == None:  # First Node is None...
            print("Linked List is Empty!!!")
        else:
            current = self.head  # Assigning 'self.head' as 'current'...
            while current != None:
                print(current.data, "---->", end = " ")
                current = current.NextNode  # Assigning 'current.NextNode' as 'current'...
                
                
                
                
    #Adding elements in the beginning of the node:-
    def insert_begin(self, data):
        new_Node = Node(data)
        if self.head == None:  # if first node is none then point to the new_node...
            self.head = new_Node  # now the first node is new_node...
        else:
            new_Node.NextNode = self.head  # the next_node of new_node is pointing to the head...
            self.head.PrevNode = new_Node  # now, the previous_node of head is pointing to the new_node...
            self.head = new_Node  # the head is now pointing to the new_node...
            
            
                
    
    # Traversing elements in the reverse direction:-
    def traverse_reverse(self):
        if self.head == None:  # First Node is None...
            print("Linked List is Empty!!!")
        else:
            current = self.head  # Assigning 'self.head' as 'current'...
            while current.NextNode != None:  # Checking whether NEXT NODE Reference is Empty...
                current = current.NextNode  # Assigning 'current.NextNode' as 'current'...
            while current != None:  # Checking whether NEXT NODE Reference is Empty or not...
                print(current.data, "---->", end = " ")
                current = current.PrevNode  # Assigning 'current.PrevNode' (i.e., PREVIOUS NODE Reference) as 'current'...
                
                
                
                
    # Adding elements in the last of the node:-
    def insert_last(self, data):
        new_Node = Node(data)
        if self.head == None:
            self.head = new_Node
        else:
            current = self.head
            while current.NextNode != None:  # checking condition...
                current = current.NextNode
            current.NextNode = new_Node
            new_Node.PrevNode = current
            
            
            
            
    # Deleting an element in the beginning:-
    def delete_begin(self):
        if self.head == None:
            print("Empty List!!")
        else:
            self.head = self.head.NextNode  # Here, head points to the next_node of head...
            self.head.PrevNode = None  # if head points to the next_node of head then, the previous_node will be empty...
            
            
            
            
    # Deleting an element from the last:-
    def delete_last(self):
        if self.head == None:
            print("Empty List!!")
        else:
            current = self.head
            while current.NextNode != None:  # checking condition...
                current = current.NextNode  # current is pointing next_node of current...
            current.PrevNode.NextNode = None  # if current is pointing next_node of current... then, the next_node of previous_node of current i.e., the last node will be empty.....
            
            
            
### DOUBLY LINKED LIST IS COMPLETED... ###


# LL1 = Doubly()
# LL1.insert_begin(20)
# LL1.insert_begin(40)
# LL1.insert_begin(60)
# LL1.insert_begin(80)
# LL1.insert_last(22)
# LL1.insert_last(42)
# LL1.insert_last(62)
# LL1.insert_last(82)
# LL1.delete_begin()
# LL1.delete_begin()
# LL1.delete_last()
# LL1.traverse_forward()
# LL1.traverse_reverse()
