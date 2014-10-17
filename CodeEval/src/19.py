import sys
test_cases = open(sys.argv[1],'r')
i = 0
for test in test_cases:
	items = test.split(',')	
	num = int(items[0])
	p1 = int(items[1])
	p2 = int(items[2])
	if p1 >=0 and p2>=0:
		mask1 = 1 << (p1-1)
		mask2 = 1 << (p2-1)
		n1 = (num & mask1) >> (p1-1)
		n2 = (num & mask2) >> (p2-1)
		if n1 == n2:
			if i != 0:
				print "\n"
			print "true",
		else:
			if i != 0:
				print "\n"
			print "false",
		i+=1	

test_cases.close()
