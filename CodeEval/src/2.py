'''
Created on Sep 18, 2014

@author: junaed
'''
import heapq
import sys

test_cases = open(sys.argv[1], 'r')
# test_cases = open("2.txt", 'r')

hq = []
elements = 0
limit = 0
smallest_length = 0
for line, test in enumerate(test_cases):
    test = str(test).strip()
    
    if line == 0:
        limit = int(test)
        continue
    
    length = len(test)
    
    if length == 0:
        continue
    if elements < limit:
        heapq.heappush(hq, (length, test))
        smallest_length = hq[0][0]
        elements += 1
    else:
        if length > smallest_length:
            heapq.heappop(hq)
            heapq.heappush(hq, (length, test))
            smallest_length = hq[0][0]
    
    pass

test_cases.close()

items = [x[1] for x in reversed(sorted(hq))]

for i, item in enumerate(items):
    sys.stdout.write(item)
    if i < limit - 1:
        sys.stdout.write("\n")
