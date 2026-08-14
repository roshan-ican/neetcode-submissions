/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    if head == nil {
		return nil
	}
	copies := make(map[*Node]*Node)

	current := head

	for current != nil {
		copies[current] = &Node{Val: current.Val}
		current = current.Next
	}
	current = head
	for current != nil {
		if current.Next != nil {
			copies[current].Next = copies[current.Next]
		}
		if current.Random != nil {
			copies[current].Random = copies[current.Random]
		}
		current = current.Next
	}
	return copies[head]
}
