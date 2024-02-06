from typing import Optional
from dataclasses import dataclass

@dataclass
class ListNode:
	val: int = 0
	next: "ListNode" = None

class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		head = ListNode(0, None)
		current = head
		while list1 and list2:
			if list1.val <= list2.val:
				current.next = ListNode(list1.val)
				list1 = list1.next
			else:
				current.next = ListNode(list2.val)
				list2 = list2.next
			current = current.next
		if list1:
			current.next = list1
		if list2:
			current.next = list2
		return head.next

def test(sol):
	test_cases = [
		(
			[ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))],
			ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))),
		),
		(
			[None, None],
			None,
		),
		(
			[ListNode(9), None],
			ListNode(9),
		),
		(
			[None, ListNode(9)],
			ListNode(9),
		),
	]
	for inp,out in test_cases:
		got = sol().mergeTwoLists(*inp)
		assert got == out, "mergeTwoLists(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(Solution)
