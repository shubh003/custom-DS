
# Node
class Node:

    """
    Node for a linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List
class LinkedList:

    """
    Linked list object with following operations:
    1. push : add element at start of linked list
    2. insertAfter : insert element after a given node
    3. append : append element at the tail of linked list
    4. deleteNodeWithData : delete node with given data
    5. deleleNodeAtPosition : delete node with given position
    6. searchNodeWithData : search node with given data
    7. searchNodeAtPosition : search node with given position
    8. swapNodes : swap nodes x and y with given data values
    9. repeatCount : count the number of occurences of given node data
    10. reverse : reverse the linked list
    11. reverseBatch : returns the head (if given) with batchwise reversed linked list
    11. sort : sort the linked list using mergesort
    12. hasLoop : find if the linked list has a loop or not
    13. findAndRemoveLoop : find and remove the loops in linked list
    14. union : takes the input as another list and returns the union of both
    15. intersection : takes the input as another list and returns the intersection of both
    14. length : length of linked list
    15. printList : print all the elemets of linked list
    """

    def __init__(self):
        self.head = None

    """
    Insertion of Node
    """
    def push(self, data):
        # Create node for given data
        new_node = Node(data)

        # Define current head as the next node for new node
        new_node.next = self.head

        # Move current head to new node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        # Check if the previous node exists
        if prev_node is None:
            raise Exception("Given previous node does not exist in LinkedList")

        # Create node for new data
        new_node = Node(new_data)

        # Move previous node's next to new node's next
        new_node.next = prev_node.next

        # Define previous node's next as new node
        prev_node.next = new_node

    def append(self, data):
        # Create node for new data
        new_node = Node(data)

        # If linked list is empty, define new node as head
        if self.head is None:
            self.head = new_node
            return

        # Iterate to reach the tail
        last = self.head
        while last.next:
            last = last.next

        # Define tail as new node
        last.next = new_node

    """
    Deletion of Node
    """
    def deleteNodeWithData(self, data):
        # Start at the head
        current = self.head

        # Check for empty list
        if current is not None:
            # Compare data for head
            if current.data == data:
                self.head = current.next
                current = None
                return

        # Iterate to find data match
        while current.next:
            if current.data == data:
                break

            previous = current
            current = current.next

        if current is None:
            return
        
        # Unlink the list
        previous.next = current.next
        current = None

    def deleteNodeAtPosition(self, position):
        # Start at the head
        current = self.head

        # If no head is there, return
        if current is None:
            return

        # If deletion of head is required
        if position == 0:
            self.head = current.next
            current = None
            return

        # Counter to keep track of position
        count = 0

        # Iterate until the position is reached
        while count != position:
            if current.next is None:
                return
            
            previous = current
            current = current.next
            count += 1

        # Unlink the linked list
        previous.next = current.next
        current = None

    """
    Search
    """
    def searchNodeWithData(self, data):
        # Start at the head
        current = self.head

        # Check for empty list
        if current is not None:
            # Compare data for head
            if current.data == data:
                return current

        # Iterate to find data match
        while current.next:
            if current.data == data:
                break

            current = current.next

        return current

    def searchNodeAtPosition(self, position):
        # Start at the head
        current = self.head

        # If no head is there, return
        if current is None:
            return

        # If head is required
        if position == 0:
            return current

        # Counter to keep track of position
        count = 0

        # Iterate until the position is reached
        while count != position:
            if current.next is None:
                return
            
            current = current.next
            count += 1

        return current

    """
    Swap
    """
    def swapNodes(self, x, y):
        if x == y:
            return

        # Search for x
        prev_x = None
        cur_x = self.head
        while cur_x is not None and cur_x.data != x:
            prev_x = cur_x
            cur_x = cur_x.next

        # Search for y
        prev_y = None
        cur_y = self.head
        while cur_y is not None and cur_y.data != y:
            prev_y = cur_y
            cur_y = cur_y.next

        # Return if any of x or y is not found
        if cur_x is None or cur_y is None:
            return

        # If x is not the head, then define prev_x.next as y
        if prev_x is not None:
            prev_x.next = cur_y
        # Else define the head of the linked list as y
        else:
            self.head = cur_y

        # If y is not the head, then define prev_y.next as x
        if prev_y is not None:
            prev_y.next = cur_x
        # Else define the head of the linked list as x
        else:
            self.head = cur_x

        # Swap the next values
        temp = cur_x.next
        cur_x.next = cur_y.next
        cur_y.next = temp

    """
    Count
    """
    def repeatCount(self, search_for):
        current = self.head

        count = 0
        # Iterate and compare data values
        while current:
            if current.data == search_for:
                count += 1

            current = current.next

        return count

    """
    Reverse
    """
    def reverse(self):
        current = self.head

        prev = None
        # Iterate and update next of each node
        while current is not None:
            temp = current.next
            current.next = prev

            prev = current
            current = temp

        # Change the head of the linked list
        self.head = prev

    def reverseBatch(self, k, head=None):
        """
        If the head is not the head of the list,
        then the function will return the pointer to the newly assigned head
        """
        if head is None:
            head = self.head
            # If the whole list is to be reversed in batches
            # Then we need to reset the head of the linked list
            head_flag = True
        else:
            head_flag = False

        current_node = head
        prev_node = None
        next_node = None 
        count = 0

        # Iterate while count < k and list has not ended
        while current_node is not None and count < k:
            next_node = current_node.next
            current_node.next = prev_node
            
            prev_node = current_node
            current_node = next_node
            count += 1

        # Reverse next batch and append to previous
        if next_node is not None:
            head.next = self.reverseBatch(k, next_node)

        if head_flag:
            self.head = prev_node
            return
        else:
            return prev_node

    """
    Loop
    """
    def hasLoop(self):
        # Floyd's Cycle-Finding Algorithm
        slow_p = self.head
        fast_p = self.head

        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                return True

        return False

    def _removeLoop(self, node_val):
        """
        Algorithm:
        1. Counter number of nodes in the loop (Suppose the number is k)
        2. Start a pointer at head and another at (head + k) node
        3. Where the two pointers meet, that is the start of the loop
        4. Define next of the previous node as null.
        """
        ptr1 = node_val
        ptr2 = node_val

        # Count number of nodes in loop
        k = 1
        while ptr1.next != ptr2:
            ptr1 = ptr1.next
            k += 1

        # Get the pointers at head and (head + k) position
        ptr1 = self.head
        ptr2 = self.head

        for _ in range(k):
            ptr2 = ptr2.next

        # Move both pointers by one step at a time until they meet
        prev = None
        while ptr1 != ptr2:
            ptr1 = ptr1.next

            prev = ptr2
            ptr2 = ptr2.next

        # Remove the connection for the loop
        prev.next = None

    def findAndRemoveLoop(self):
        # Floyd's Cycle-Finding Algorithm
        slow_p = self.head
        fast_p = self.head

        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                self._removeLoop(slow_p)

                return True

        return False

    """
    Sort
    """
    def _splitHalf(self, head_ref):
        # Check if the linked list is depleted
        if head_ref is None or head_ref.next is None:
            return head_ref, None

        # Split the list into two parts using slow and fast pointers
        slow_p = head_ref
        fast_p = head_ref.next

        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        # Remove the connection and split
        first_half = head_ref
        second_half = slow_p.next
        slow_p.next = None

        return first_half, second_half

    def _sortedMerge(self, node_a, node_b):
        result = None

        # Check if first half of list is depleted
        if node_a is None:
            return node_b

        # Check if second half of list is depleted
        if node_b is None:
            return node_a

        # Compare data values and append the respective node to result
        if node_a.data <= node_b.data:
            result = node_a
            result.next = self._sortedMerge(node_a.next, node_b)
        else:
            result = node_b
            result.next = self._sortedMerge(node_a, node_b.next)

        return result


    def _mergeSort(self, head_ref):
        # If linked list is emply or count is one, return linked list
        if head_ref is None or head_ref.next is None:
            return head_ref

        first_half, second_half = self._splitHalf(head_ref)

        # Recursively merge first and second half
        sorted_first = self._mergeSort(first_half)
        sorted_second = self._mergeSort(second_half)

        # Merge sorted first and second halves
        sorted_head_ref = self._sortedMerge(sorted_first, sorted_second)

        return sorted_head_ref


    def sort(self):
        # Sort given list
        result = self._mergeSort(self.head)

        # Change the head of the list
        self.head = result

    """
    Operations
    """
    def intersection(self, llist2):
        # Check if the llist is blank
        if llist2 is None:
            return

        # Sort the lists using merge sorts
        self.sort()
        llist2.sort()

        # Start with the heads of both lists
        temp1 = self.head
        temp2 = llist2.head

        result = None
        prev = None
        # Iterate until any one of the list is depleted
        while temp1 and temp2:
            # Iterate until temp2 is iterated to match the data value
            while temp2 and temp1.data > temp2.data:
                temp2 = temp2.next

            # If temp2 gets depleted then break
            if temp2 is None:
                break

            # If data is matched, append the corresponding node to the result
            if temp1.data == temp2.data:
                append_node = Node(temp1.data)
                # Append node if result exists
                if result is not None:
                    prev.next = append_node
                    # Keep track of the node which was last inserted
                    prev = append_node
                else:
                    # Create the linked list for result
                    result = LinkedList()
                    result.head = append_node

                    prev = result.head
            
            temp1 = temp1.next

        # Return the intersection as a linked list
        return result

    def union(self, llist2):
        # Check if the list to be appended is blank
        if llist2 is None:
            return self

        # Sort the lists using merge sorts
        self.sort()
        llist2.sort()

        # Start with the heads of both lists
        temp1 = self.head
        temp2 = llist2.head

        result = None
        prev = None
        # Iterate until any one of the list is depleted
        while temp1 and temp2:
            # Check which of temp1 and temp2 has lower data value
            if temp1.data < temp2.data:
                append_node = Node(temp1.data)
                temp1 = temp1.next
            elif temp2.data < temp1.data:
                append_node = Node(temp2.data)
                temp2 = temp2.next
            else:
                # If data values are equal, move both the pointers
                append_node = Node(temp1.data)
                temp1 = temp1.next
                temp2 = temp2.next

            print append_node.data

            # Append data to the result
            if result is not None:
                prev.next = append_node
                prev = append_node
            else:
                result = LinkedList()
                result.head = append_node

                prev = result.head

        # Check if any of temp1 or temp2 is not depleted
        if temp1 is not None:
            prev.next = temp1

        if temp2 is not None:
            prev.next = temp2

        # Return the intersection as a linked list
        return result

    """
    Length of linked list
    """
    @property
    def length(self):
        count = 0

        current = self.head

        # Iterate and increment until the end of the linked list is reached
        while current:
            count += 1
            current = current.next
        
        return count

    """
    Print List
    """
    def printList(self):
        temp = self.head

        while temp:
            print temp.data
            temp = temp.next