# Creating a Node:-

class Node(object):
    def __init__(self, data):
        self.data = data
        self.NextNode = None  # Reference/Next Node is equal to Empty!!!

# Creating a Linked List:-
class LinkedList(object):
    def __init__(self):
        self.head = None # Linked List is Empty!!!
    
    
    
    # Traversing an element:-
    def traversal(self):
        if self.head == None:
            print("Linked List is Empty!!!")
        else:
            n = self.head  # Assigning self.head as variable 'n'...
            while n != None:
                print(n.data, "----->", end = " ")
                n = n.NextNode  # Assigning n.NextNode as variable 'n' within the 'while' loop...
    
    
    
    # Inserting an element in the beginning of a node:-
    def insert_begin(self, data):
        new_Node = Node(data)  # Creating a New Node...
        new_Node.NextNode = self.head
        self.head = new_Node
        
        
        
    # Inserting an element at the last of the node:-
    def insert_last(self, data):
        new_Node = Node(data)  # Creating a New Node...
        if self.head == None:
            self.head = new_Node
        else:
            n = self.head  # Assigning self.head as variable 'n'...
            while n.NextNode != None:
                n = n.NextNode  # Assigning n.NextNode as variable 'n' within the 'while' loop...
            n.NextNode = new_Node
            
            
            
            
    # Inserting an element after a node:-
    def insert_after(self, data, x):
        n = self.head  # Assigning self.head as variable 'n'...
        while n != None:
            if x == n.data:
                break
            n = n.NextNode  # Assigning n.NextNode as variable 'n' for the 'else' part of the if-else case...
        if n == None:
            print("Node is not present!!!")
        else:
            new_Node = Node(data)
            new_Node.NextNode = n.NextNode
            n.NextNode = new_Node
            
            
            
            
    # Deleting the first Node from the beginning of the Linked List:-
    def delete_first(self):
        if self.head == None:
            print("Linked List is Empty!!!")
        else:
            self.head = self.head.NextNode
            
            
            
            
    # Deleting the last Node from the ending of the Linked List:-
    def delete_last(self):
        if self.head == None:
            print("Linked List is Empty!!!")
        else:
            n = self.head
            while n.NextNode.NextNode != None:
                n = n.NextNode
            n.NextNode = None
            
            
            
            
### WITHIN THE OUTPUT SECTION:-
### TYPE:-

### FIRST OUTPUT COLUMN:-
LL1 = LinkedList()
LL1.insert_begin(10)
LL1.insert_begin(20)
LL1.insert_begin(30)
LL1.insert_begin(40)
LL1.traversal()

### SECOND OUTPUT COLUMN:-
LL1 = LinkedList()
LL1.insert_last(10)
LL1.insert_last(20)
LL1.insert_last(30)
LL1.insert_last(40)
LL1.traversal()

### THIRD OUTPUT COLUMN:-
LL1 = LinkedList()
LL1.insert_begin(10)
LL1.insert_begin(10.5)
LL1.insert_begin(20)
LL1.insert_after(15, 10.5)
LL1.traversal()

### FOURTH OUTPUT COLUMN:-
LL1 = LinkedList()
LL1.insert_last(20)
LL1.insert_last(40)
LL1.insert_last(60)
LL1.delete_first()
LL1.traversal()
