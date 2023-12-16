from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		return "Node(%s, %s)" % (self.val, self.next)

	def __eq__(self, other):
		if other is None:
			return False
		if self.val != other.val:
			return False
		return self.next == other.next

class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		out = ListNode()
		prev = out
		carry = 0
		while not (l1 is None and l2 is None and carry == 0):
			n = carry
			if l1 is not None:
				n += l1.val
				l1 = l1.next
			if l2 is not None:
				n += l2.val
				l2 = l2.next
			prev.next = ListNode(n%10)
			prev = prev.next
			carry = n//10
		return out.next

class SolutionRecursive:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		return self.addTwoNumbersAux(l1, l2, 0)

	def addTwoNumbersAux(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
		if l1 is None and l2 is None:
			if carry == 0:
				return None
			else:
				return ListNode(carry)
		n = carry
		if l1 is not None:
			n += l1.val
		if l2 is not None:
			n += l2.val
		val = n%10
		carry = n//10
		l1 = l1.next if l1 is not None else None
		l2 = l2.next if l2 is not None else None
		return ListNode(val, self.addTwoNumbersAux(l1, l2, carry))

def test():
	test_cases = [
		(
			[
				ListNode(2, ListNode(4, ListNode(3))),
				ListNode(5, ListNode(6, ListNode(4))),
			],
			ListNode(7, ListNode(0, ListNode(8))),
		),
		(
			[
				ListNode(0),
				ListNode(0),
			],
			ListNode(0),
		),
		(
			[
				ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
				ListNode(9),
			],
			ListNode(8, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))),
		),
		(
			[
				ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
				ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
			],
			ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1)))))))),
		),
	]
	for inp,out in test_cases:
		got = Solution().addTwoNumbers(*inp)
		assert got == out, "addTwoNumbers(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test()
