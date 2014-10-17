import sys

test_cases =  open(sys.argv[1], 'r')
for test in test_cases:
	nums = test.split(',')
	x = int(nums[0])
	n = int(nums[1])
	i = 1
	while x > i*n:
		i+=1

	print i*n
test_cases.close()
