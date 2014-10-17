import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	#data = [float(v) for v in test.split(' ')]
	data = [v.rstrip('\n') for v in test.split(' ')]
	data.sort(key=float)
	for a in data:
		print a,
	print "\n"
test_cases.close()
