class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		idx = dict()
		for i in range(len(nums)):
			other = target-nums[i]
			if other in idx:
				idx[other].append(i)
			else:
				idx[other] = [i]
		for i in range(len(nums)):
			b = idx.get(nums[i])
			if b is not None:
				for j in b:
					if i != j:
						return [i, j]

class SolutionSlow:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		for i in range(len(nums)):
			for j in range(len(nums)):
				if i == j:
					continue
				if nums[i] + nums[j] == target:
					return [i, j]

def test():
	test_cases = [
		([[2, 7, 11, 15], 9], [0, 1]),
		([[3, 2, 4], 6], [1, 2]),
		([[3, 3], 6], [0, 1]),
	]
	for inp,out in test_cases:
		got = Solution().twoSum(*inp)
		assert got == out, "twoSum(%s) = %s, want %s" % (inp, got, out)

if __name__ == "__main__":
	test()
