"""
SINGLE FLIGHT AIRLINE TICKET RESERVATION SYSTEM
This program implements a simple airline ticket reservation system for a single flight
using an alphabetized linked list to store passenger names.
"""

class PassengerNode:
    """
    Node class representing a single passenger in the linked list
    
    Attributes:
        name (str): The passenger's name
        next (PassengerNode): Reference to the next node in the linked list
    """
    def __init__(self, name):
        # Initialize node with passenger name and set next pointer to None
        self.name = name    # Store the passenger's name
        self.next = None    # Pointer to the next node in the list

class SingleFlightReservation:
    """
    Main class for the single flight reservation system
    
    This class manages a linked list of passengers in alphabetical order
    and provides operations for ticket reservation management.
    
    Time Complexity: O(n) for all operations where n = number of passengers
    Space Complexity: O(n) where n = number of passengers
    
    Attributes:
        head (PassengerNode): The first node in the passengers linked list
    """
    def __init__(self):
        # Initialize an empty linked list (no passengers initially)
        self.head = None  # Head pointer starts as None (empty list)
    
    def reserve_ticket(self, name):
        """
        Reserve a ticket for a passenger and maintain alphabetical order
        
        Steps:
        1. Validate and format the name
        2. Create a new node for the passenger
        3. Find the correct alphabetical position
        4. Insert the node while maintaining sorted order
        
        Time Complexity: O(n) - may need to traverse entire list in worst case
        Space Complexity: O(1) - only creates one new node
        
        Args:
            name (str): The passenger's name to reserve
            
        Returns:
            bool: True if reservation successful, False if duplicate exists
        """
        # Clean and format the input name (title case, remove extra spaces)
        name = name.strip().title()
        
        # Create a new node for the passenger
        new_node = PassengerNode(name)
        
        # CASE 1: Empty list OR new name should be at beginning
        # If list is empty or new name comes before current head alphabetically
        if not self.head or name < self.head.name:
            # Insert at beginning: new node points to current head
            new_node.next = self.head
            # Update head to point to new node
            self.head = new_node
            print(f" Ticket reserved for {name}")
            return True
        
        # CASE 2: Check for duplicate reservation
        # Search through list to see if passenger already exists
        if self._find_passenger(name):
            print(f" {name} already has a reservation")
            return False
        
        # CASE 3: Insert in middle or end of list
        # Start from head and traverse to find insertion point
        current = self.head
        # Traverse until we find where to insert (alphabetical order)
        while current.next and current.next.name < name:
            current = current.next
        
        # Insert the new node between current and current.next
        new_node.next = current.next  # New node points to current's next
        current.next = new_node       # Current points to new node
        
        print(f" Ticket reserved for {name}")
        return True
    
    def cancel_reservation(self, name):
        """
        Cancel a passenger's reservation by removing their node from the list
        
        Steps:
        1. Search for the passenger in the list
        2. Remove the node and reconnect the list
        3. Handle special cases (head node, node not found)
        
        Time Complexity: O(n) - may need to traverse entire list
        Space Complexity: O(1) - no additional space used
        
        Args:
            name (str): The passenger's name to cancel
            
        Returns:
            bool: True if cancellation successful, False if passenger not found
        """
        # Clean and format the input name
        name = name.strip().title()
        
        # Check if list is empty
        if not self.head:
            print(" No reservations exist")
            return False
        
        # CASE 1: Removing the head node
        if self.head.name == name:
            # Move head pointer to next node, effectively removing current head
            self.head = self.head.next
            print(f" Reservation canceled for {name}")
            return True
        
        # CASE 2: Removing from middle or end of list
        # Start from head and search for the node to remove
        current = self.head
        # Traverse until we find the node BEFORE the one we want to remove
        while current.next and current.next.name != name:
            current = current.next
        
        # If we reached end without finding the passenger
        if not current.next:
            print(f" No reservation found for {name}")
            return False
        
        # Remove the node by skipping over it
        # current.next points to the node we want to remove
        # We make current.next point to the node AFTER the one we're removing
        current.next = current.next.next
        print(f" Reservation canceled for {name}")
        return True
    
    def check_reservation(self, name):
        """
        Check if a passenger has a reservation by searching the linked list
        
        Time Complexity: O(n) - may need to traverse entire list
        Space Complexity: O(1) - no additional space used
        
        Args:
            name (str): The passenger's name to check
            
        Returns:
            bool: True if reservation exists, False otherwise
        """
        # Clean and format the input name
        name = name.strip().title()
        current = self.head  # Start from head of list
        
        # Linear search through the linked list
        while current:
            # If we found the passenger
            if current.name == name:
                print(f" {name} has a reservation")
                return True
            # Move to next node
            current = current.next
        
        # If we didn't find the passenger after traversing entire list
        print(f" {name} does not have a reservation")
        return False
    
    def display_passengers(self):
        """
        Display all passengers in alphabetical order
        
        Time Complexity: O(n) - must traverse entire list
        Space Complexity: O(1) - only uses temporary variables
        
        This method provides a visual representation of all current reservations
        """
        # Check if list is empty
        if not self.head:
            print("No passengers have reservations")
            return
        
        # Display header
        print("\n Passenger List (Alphabetical Order):")
        print("-" * 40)  # Visual separator
        
        # Traverse the linked list and print each passenger
        current = self.head  # Start from head
        count = 1  # Counter for passenger numbering
        
        while current:
            # Print passenger with number
            print(f"{count}. {current.name}")
            # Move to next node
            current = current.next
            count += 1
        
        print("-" * 40)  # Visual separator
    
    def _find_passenger(self, name):
        """
        Private helper method to find a passenger node in the linked list
        
        This is used internally to check for duplicates before insertion
        and for other internal operations.
        
        Time Complexity: O(n) - linear search
        Space Complexity: O(1) - only uses temporary variables
        
        Args:
            name (str): The passenger name to find
            
        Returns:
            PassengerNode: The node if found, None otherwise
        """
        current = self.head  # Start from head
        
        # Linear search through linked list
        while current:
            # Check if current node matches the name
            if current.name == name:
                return current  # Return the node if found
            current = current.next  # Move to next node
        
        return None  # Return None if not found

def main_single_flight():
    """
    Main function that runs the single flight reservation system
    
    This function provides the user interface and menu system
    for interacting with the reservation system.
    """
    # Create an instance of the reservation system
    system = SingleFlightReservation()
    
    # Main program loop - continues until user chooses to exit
    while True:
        # Display menu header
        print("\n" + "="*50)
        print("        AIRLINE TICKET RESERVATION SYSTEM")
        print("                  (Single Flight)")
        print("="*50)
        
        # Display menu options
        print("1. Reserve Ticket")
        print("2. Cancel Reservation") 
        print("3. Check Reservation")
        print("4. Display Passengers")
        print("5. Exit")
        print("-"*50)
        
        # Get user input
        choice = input("Enter your choice (1-5): ").strip()
        
        # Process user choice
        if choice == '1':
            # Reserve ticket option
            name = input("Enter passenger name: ").strip()
            if name:  # Validate input is not empty
                system.reserve_ticket(name)
            else:
                print(" Invalid name")
                
        elif choice == '2':
            # Cancel reservation option
            name = input("Enter passenger name to cancel: ").strip()
            if name:  # Validate input is not empty
                system.cancel_reservation(name)
            else:
                print(" Invalid name")
                
        elif choice == '3':
            # Check reservation option
            name = input("Enter passenger name to check: ").strip()
            if name:  # Validate input is not empty
                system.check_reservation(name)
            else:
                print("Invalid name")
                
        elif choice == '4':
            # Display all passengers
            system.display_passengers()
            
        elif choice == '5':
            # Exit program
            print("👋 Thank you for using the reservation system!")
            break  # Exit the while loop
            
        else:
            # Handle invalid menu choices
            print(" Invalid choice. Please enter 1-5.")

# Standard Python idiom to run the main function when script is executed directly
if __name__ == "__main__":
    main_single_flight()


    