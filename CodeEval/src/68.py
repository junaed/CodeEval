import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	test = test.rstrip('\n')
	data = list(test)
	stack = []
	result = "True"
	for item in data:
		if item == '(' or item =='{' or item == '[':
			stack.append(item)
		elif len(stack)>0:
			top = stack.pop()
			if top == '(' and item != ')':
				result = "False"
				break
			elif top == '{' and item != '}':
				result = "False"
				break	
			elif top =='[' and item != ']':
				result = "False"
				break
			else:
				pass
		else:
			result = "False"
			break
	if result == "False":
		print result
	elif len(stack)==0:
		print result
	else:
		print "False"
test_cases.close()
