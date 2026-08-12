class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        // 1. Properly instantiate the dummy node
        let dummyNode = new ListNode(0);
        let tail = dummyNode;

        // 2. Check if both pointers are valid (not null)
        while (list1 && list2) {
            if (list1.val <= list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }

        // 3. Attach remaining nodes from list1 or list2
        if (list1) {
            tail.next = list1;
        } else {
            tail.next = list2;
        }

        // 4. Return matching variable name
        return dummyNode.next;
    }
}