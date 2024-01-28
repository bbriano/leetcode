from typing import Optional
from dataclasses import dataclass

@dataclass
class ListNode:
	val: int
	next: "ListNode" = None

	def __eq__(self, other: "ListNode") -> bool:
		if type(self) != type(other):
			return False
		if self.val != other.val:
			return False
		return self.next == other.next

class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		head = ListNode(0, head)
		cur = head
		for _ in range(n):
			cur = cur.next
		ref = head
		while cur.next != None:
			cur = cur.next
			ref = ref.next
		ref.next = ref.next.next
		return head.next

def test(sol):
	test_cases = [
		(
			[ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2],
			ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
		),
		(
			[ListNode(1, ListNode(2)), 1],
			ListNode(1),
		),
		(
			[ListNode(1), 1],
			None,
		),
	]
	for inp,out in test_cases:
		got = sol().removeNthFromEnd(*inp)
		assert got == out, "removeNthFromEnd(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test(Solution)
	from timeit import timeit
	print(timeit('test(Solution)', globals=globals()))
