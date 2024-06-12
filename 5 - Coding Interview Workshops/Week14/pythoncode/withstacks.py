'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
#Initialize a Node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#LinkedList1 (L1)
node1 = ListNode(7)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(3)
#L1 = 7->2->4->3
node1.next = node2
node1.next.next = node3
node1.next.next.next = node4

#LinkedList2 (L2)
nodea = ListNode(5)
nodeb = ListNode(6)
nodec = ListNode(4)
#L2 = 5 -> 6 -> 4
nodea.next = nodeb
nodea.next.next = nodec


def add_two_numbers(l1, l2):
    stack1, stack2 = [], []
    
    # Push all values from l1 to stack1
    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    
    # Push all values from l2 to stack2
    while l2:
        stack2.append(l2.val)
        l2 = l2.next
    
    carry = 0
    result = None
    
    # While there are values in either stack or there is a carry
    while stack1 or stack2 or carry:
        sum_val = carry
        
        if stack1:
            sum_val += stack1.pop()
        
        if stack2:
            sum_val += stack2.pop()
        
        carry = sum_val // 10
        sum_val = sum_val % 10
        
        # Create a new node with the current sum_val
        new_node = ListNode(sum_val)
        new_node.next = result
        result = new_node
    
    return result

# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

result = add_two_numbers(node1, nodea)
print_linked_list(result)
