class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

head = node1

# [1,2,3]

def convertToArray(head):
    array = []
    currNode = head  # Node(1)

    while currNode:
        array.append(currNode.value)
        currNode = currNode.next # None

    return array


# print(convertToArray(head))

def addNodeAtStart(head,new_value):
    new_node = Node(new_value) #Node(4) --> Node(1)
    if not head:
        return new_node
    
    new_node.next = head # Node(1)
    head = new_node # Node(4)

    return head

# head = addNodeAtStart(head,4) # Node(4)
# print(convertToArray(head))

def addAtAnyPosition(head,new_value,prev_node): # -1 -> 1 -> 2 -> x = 4  -> 3
    new_node = Node(new_value)

    # print(prev_node.value,head.value,new_node.value)
    new_node.next = prev_node.next #Node(1)
    prev_node.next = new_node

    

    return head

dummy_node = Node(None)
dummy_node.next = head
# head = addAtAnyPosition(head,-1,dummy_node)
# head = dummy_node.next
# print(convertToArray(head))

def removeAtHead(head): # 1 2 3
    head = head.next
    return head

# head = removeAtHead(head)
# print(convertToArray(head))


def removeAtAnyPosition(head,postion): # 1 2 3  #1 
    dummy_node = Node(None)
    dummy_node.next = head
    currNode = head
    prevNode = dummy_node
    index = 0

    while currNode.next and index < postion:
        prevNode = currNode  #Node(1)
        currNode = currNode.next # Node(2)
        index += 1

    prevNode.next = currNode.next  # Node(2)

    return dummy_node.next

head = removeAtAnyPosition(head,1)
print(convertToArray(head))


    






