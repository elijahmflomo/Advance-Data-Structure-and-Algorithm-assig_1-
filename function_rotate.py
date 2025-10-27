# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to print linked list
def printList(head):
    current = head
    while current:
        print(current.data, end=" → " if current.next else "")
        current = current.next
    print()

# Function to rotate linked list by k nodes
def rotateLinkedList(head, k):
    if head is None or k == 0:
        return head

    # Step 1: Traverse to the kth node
    current = head
    count = 1
    while count < k and current is not None:
        current = current.next
        count += 1

    # If k is more than the number of nodes, return original list
    if current is None:
        return head

    # kth node
    kthNode = current

    # Step 2: Go to the last node
    while current.next is not None:
        current = current.next

    # Step 3: Connect last node to head
    current.next = head

    # Step 4: New head is (k+1)th node
    new_head = kthNode.next

    # Step 5: Break the list at kth node
    kthNode.next = None

    return new_head

# ------------------------
# Example Usage
# ------------------------
# Creating the linked list: 10 → 20 → 30 → 40 → 50
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Original Linked List:")
printList(head)

k = 2
head = rotateLinkedList(head, k)

print(f"Linked List after rotating by {k} nodes:")
printList(head)



"""Explanation of Steps

Traverse to the kth node → This is where we split the list.

Go to the last node → So we can connect it to the original head.

Break the link at kth node → So the new list starts at (k+1)th node.

Return new head → Now the list is rotated.

Time and Space Complexity

Time Complexity: O(n) → Traverse list twice (once to kth node, once to last node)

Space Complexity: O(1) → Only pointers are used"""
