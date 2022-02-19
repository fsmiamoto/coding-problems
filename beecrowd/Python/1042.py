nums = (int(x) for x in input().split())
[print(n) for n in nums]
antes = nums.copy()
nums.sort()

for n in nums:
	print(n)

print('')

for n in antes:
	print(n)