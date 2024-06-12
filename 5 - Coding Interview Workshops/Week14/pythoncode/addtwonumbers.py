'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
#Initialize a Node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#Reverse the linked list
def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

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


'''
Add two numbers function
Takes in LinkedList1 and LinkedList2
Reverses the LinkedLists
Calculates its sum

Time Complexity: O(n1 + n2)
Space Complexity: O(max(n1, n2))
'''
#Time Complexity -> O(n1) + O(n2) + O(max(n1, n2)) === O(n1 + n2)
#Space Complexity -> O(max(n1, n2))
def add_two_numbers(l1, l2):
    reversed_l1 = reverse_list(l1) #O(n1)
    reversed_l2 = reverse_list(l2) #O(n2)

    carry = 0
    result = ListNode(0)
    current = result
    #initialization of sum
    while reversed_l1 is not None or reversed_l2 is not None or carry: #O(max(n1, n2))

        sum_val = carry
        if reversed_l1 is not None:
            sum_val += reversed_l1.val
            reversed_l1 = reversed_l1.next
        
        if reversed_l2 is not None:
            sum_val += reversed_l2.val
            reversed_l2 = reversed_l2.next

        carry = sum_val // 10 #takes the dividend
        current.next = ListNode(sum_val % 10)
        current = current.next

    if carry == 1:
        current.next = ListNode(1)
    
    return reverse_list(result.next)

def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next


added = add_two_numbers(node1, nodea)
print_linked_list(added)