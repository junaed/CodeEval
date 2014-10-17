'''
Created on Sep 18, 2014

@author: junaed
'''

import sys
test_cases = open(sys.argv[1], 'r')
# test_cases = open("30.txt", 'r')
for line, test in enumerate(test_cases):
    inputs = str(test).split(";")
    
    flist = [int(x) for x in str(inputs[0]).split(",")]
    slist = [int(x) for x in str(inputs[1]).split(",")]
    
    min_elements = max(len(flist), len(slist))
    i=0
    j=0
    common_elements = []
    for k in xrange(0,min_elements):
        if i<len(flist) and j<len(slist):
            if flist[i] == slist[j]:
                common_elements.append(flist[i])
                i+=1
                j+=1
            elif flist[i] < slist[j]:
                i+=1
            else:
                j+=1
        else:
            break
    for i, item in enumerate(common_elements):
        if i >0: 
            sys.stdout.write(",")
        sys.stdout.write(str(item))
                 
    sys.stdout.write("\n")
    
    pass

test_cases.close()