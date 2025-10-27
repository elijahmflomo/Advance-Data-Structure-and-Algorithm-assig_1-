# Node class for circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to print a circular linked list
def printCircularList(head):
    if not head:
        return
    current = head
    while True:
        print(current.data, end=" → " if current.next != head else " → (back to head)")
        current = current.next
        if current == head:
            break
    print()

# Function to split circular linked list into two halves
def splitCircularList(head):
    if head is None or head.next == head:
        # Only one node or empty list
        return head, None

    slow = head
    fast = head

    # Step 1: Find middle using slow and fast pointers
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Set heads for the two halves
    head1 = head
    head2 = slow.next

    # Step 3: Make the first half circular
    slow.next = head1

    # Step 4: Make the second half circular
    current = head2
    while current.next != head:
        current = current.next
    current.next = head2

    return head1, head2

# ------------------------
# Example Usage
# ------------------------

# Example 1: Odd number of nodes
head_odd = Node(1)
head_odd.next = Node(2)
head_odd.next.next = Node(3)
head_odd.next.next.next = Node(4)
head_odd.next.next.next.next = Node(5)
head_odd.next.next.next.next.next = head_odd  # circular link

print("Original Circular Linked List (Odd):")
printCircularList(head_odd)

first_half, second_half = splitCircularList(head_odd)

print("First Half:")
printCircularList(first_half)
print("Second Half:")
printCircularList(second_half)

# Example 2: Even number of nodes
head_even = Node(10)
head_even.next = Node(20)
head_even.next.next = Node(30)
head_even.next.next.next = Node(40)
head_even.next.next.next.next = Node(50)
head_even.next.next.next.next.next = Node(60)
head_even.next.next.next.next.next.next = head_even  # circular link

print("\nOriginal Circular Linked List (Even):")
printCircularList(head_even)

first_half_even, second_half_even = splitCircularList(head_even)

print("First Half:")
printCircularList(first_half_even)
print("Second Half:")
printCircularList(second_half_even)


"""Step-by-Step Explanation

Find the middle node using slow and fast pointers:

slow moves 1 step, fast moves 2 steps.

When fast reaches the end (or just before head), slow is at the middle.

Split the list:

head1 = head → first half starts at head.

head2 = slow.next → second half starts after middle.

Make both halves circular:

slow.next = head1 → first half circular.

Traverse second half to last node → current.next = head2.


Boundary Cases
Case	                             Example	Explanation
Odd number of nodes	                 5 nodes	First half has 3 nodes, second half has 2 nodes
Even number of nodes	             6 nodes	Both halves have 3 nodes
Single node	                         1 node	    Only first half exists, second half = None
Empty list	                         0 nodes	Both halves = None


Time and Space Complexity

Time Complexity: O(n) → traverse list once to find middle and once for second half.

Space Complexity: O(1) → only pointers are used."""