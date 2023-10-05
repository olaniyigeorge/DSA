

class LinkedList():
    node_list = []
    depth=0
    node ={}

    def __init__(self, first_node_val=None):
        if first_node_val:
            node ={}
            node["val"] = self.first_node_val
            print(node.val())    
            self.depth += self.depth
            node["depth"] = self.depth
            print(node.dep())
            node["next"] = {}
            print(node.next())

            self.node_list.append(node)
        

    def __str__(self):
        # for node in self.node_list:
        #     print(node)
        if self.depth== 0:
            return f"Empty LinkedList created."
        return f"{self.node_list}"
    
    def add(self, value):
        '''
        Creates a dictionary to hold the value in val and an
        empty dictionary for the next node
        '''
        if self.depth == 0:
            print(f'making node  {self.depth + 1} first')
            first_node ={}
            first_node["val"] = value
            print(first_node["val"])    
            self.depth += 1
            first_node["depth"] = self.depth
            print(first_node["depth"])
            first_node["child"] = {}
            print(first_node["child"])

            self.node_list.append(first_node)
            print(first_node)
        else:
            print(f'making node {self.depth + 1}')
            
            parent_node =self.node_list[-1]
            print(parent_node)

            child_node= {}
            child_node["val"] = value
            print(child_node["val"])    
            self.depth += 1
            child_node["depth"] = self.depth
            print(child_node["depth"])
            child_node["child"] = {}
            print(child_node["child"])

            parent_node["child"].update(child_node)
            print(parent_node)
        

## create a linkedlist : basically a List of distionaries
## Add node(dictionary) to lisked_list
## node(dictionary0 has this shape)


l= LinkedList()
print(l)

print("-----------")

l.add(40)
print(l)

print("------------")

l.add(50)
print(l)


class Node():

    def __init__(self, data,  next=None, parent=None):
        self.data = data
        self.parent = parent
        self.next_node = next

class LinkedList():

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next_node
        print()


lst= LinkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.display()
