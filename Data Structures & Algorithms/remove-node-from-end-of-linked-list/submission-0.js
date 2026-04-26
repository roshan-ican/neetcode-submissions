/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {

        let current = head
        let count = 0
        while(current !== null){
            count++
            current = current.next
        }
        let target = count - n
        if (target === 0) {
            return head.next
        }
            // Step 3: Find node before target and remove target
        current = head
        for (let i = 0; i < target - 1; i++) {
            current = current.next
        }
        // Remove the nth node from end
        current.next = current.next.next
        
        return head

    
    }
}
