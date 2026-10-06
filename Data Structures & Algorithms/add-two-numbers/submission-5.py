# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        dummy = ListNode(0)
        curr = dummy

        carry = 0

        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0

            add = val1 + val2 + carry

            digit = add % 10
            carry = add // 10

            curr.next = ListNode(digit)
            curr = curr.next

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        return dummy.next
        