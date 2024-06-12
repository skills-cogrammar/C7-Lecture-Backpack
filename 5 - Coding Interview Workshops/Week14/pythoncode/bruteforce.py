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


def linked_list_to_integer(node):
    num = 0
    while node:
        num = num * 10 + node.val
        node = node.next
    return num

def integer_to_linked_list(num):
    # Handle the special case of zero
    if num == 0:
        return ListNode(0)
    
    head = None
    while num > 0:
        num, digit = divmod(num, 10)
        new_node = ListNode(digit)
        new_node.next = head
        head = new_node
    return head

def add_two_numbers(l1, l2):
    # Convert linked lists to integers
    num1 = linked_list_to_integer(l1)
    num2 = linked_list_to_integer(l2)
    
    # Add the two numbers
    total = num1 + num2
    
    # Convert the result back to a linked list
    return integer_to_linked_list(total)


def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next



results = add_two_numbers(node1, nodea)
print_linked_list(results)