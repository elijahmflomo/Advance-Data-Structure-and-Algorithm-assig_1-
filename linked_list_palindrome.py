# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to print linked list (for testing)
def printList(head):
    current = head
    while current:
        print(current.data, end=" → " if current.next else "")
        current = current.next
    print()

# Function to reverse a linked list
def reverseList(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # new head of reversed list

# Function to check if linked list is a palindrome
def isPalindrome(head):
    if head is None or head.next is None:
        return True  # Empty or single node list is palindrome

    # Step 1: Find middle of the list
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    second_half_start = reverseList(slow.next)

    # Step 3: Compare first and second half
    first_half = head
    second_half = second_half_start
    result = True
    while second_half:
        if first_half.data != second_half.data:
            result = False
            break
        first_half = first_half.next
        second_half = second_half.next

    # Step 4: Restore the original list
    slow.next = reverseList(second_half_start)

    return result

# ------------------------
# Example Usage
# ------------------------
# Creating a linked list: 1 → 2 → 3 → 2 → 1
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print("Original Linked List:")
printList(head)

if isPalindrome(head):
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")

print("Linked List after checking (restored):")
printList(head)


"""Step-by-Step Explanation

Find the middle:

Use slow (1 step) and fast (2 steps) pointers.

When fast reaches the end, slow is at the middle.

Reverse the second half:

Reversing is done in place, so O(1) space.

Compare halves:

Compare nodes from the first half and reversed second half.

If all match → palindrome

Restore the list:

Reverse the second half again to restore original linked list.



Complexity Analysis

Time Complexity: O(n)

Traverse list to find middle → O(n/2)

Reverse second half → O(n/2)

Compare halves → O(n/2)

Restore list → O(n/2)

Space Complexity: O(1)

Only pointers used, no extra arrays or stacks"""
