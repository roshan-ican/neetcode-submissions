"""cscc
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        something = {None: None}

        curr = head
        while curr:
            something[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: connect next and random
        curr = head

        while curr:
            copy = something[curr]

            copy.next = something[curr.next]
            copy.random = something[curr.random]

            curr = curr.next

        return something[head]
