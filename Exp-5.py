
# Experiment 5: Singly Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data  # The value of the node
        self.next = None  # The pointer to the next node (initially None)

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head as None (empty list)

    def is_empty(self):
        return self.head is None  # Return True if the list is empty

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Link the last node to the new node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Make the new node point to the current head
        self.head = new_node  # Set the new node as the head

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:  # If the node to be deleted is the head
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:  # Find the node with the given key
            prev = current
            current = current.next
        if current is None:  # If the key was not found in the list
            print("Node with value", key, "not found.")
            return
        prev.next = current.next  # Unlink the node to be deleted
        current = None  # Free memory (optional in Python)

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:  # Node with the key found
                return True
            current = current.next
        return False  # Node with the key not found

    def display(self):
        if self.is_empty():
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end="   - > ")
            current = current.next
        print("None")  # Indicate the end of the list

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move prev to the current node
            current = next_node  # Move to the next node
        self.head = prev  # Set the new head to the last node

# Example Usage
linked_list = SinglyLinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_beginning(5)
print("Linked List after insertion:")
linked_list.display()  # Display the list
linked_list.delete_node(20)
print("\nLinked List after deleting node with value 20:")
linked_list.display()  # Display the list after deletion
found = linked_list.search(30)
print("\nIs 30 present in the list?", found)
linked_list.reverse()
print("\nLinked List after reversing:")
linked_list.display()  # Display the reversed list
