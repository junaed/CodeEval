import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	strings = test.split(',')
	merged = strings[1].rstrip('\n')+strings[1].rstrip('\n')
	if merged.find(strings[0]) != -1:
		print "True"
	else:
		print "False"	

test_cases.close()
