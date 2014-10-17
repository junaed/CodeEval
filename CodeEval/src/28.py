'''
Created on Sep 18, 2014

@author: junaed
'''

import sys

def match_char(in1, in2, id1, id2):
    if in1[id1] == in2[id2]:
        return True
    else:
        return False

test_cases = open(sys.argv[1], 'r')
# test_cases = open("28.txt", 'r')
for line, test in enumerate(test_cases):
    test = str(test).strip()
    inputs = test.split(",")
    
    len1 = len(inputs[0])
    len2 = len(inputs[1])
    if line > 0:
        sys.stdout.write("\n")
#     if len2 > len1:
#         sys.stdout.write("false")
#         continue
        
    j = 0
    i = 0
    match = "false"
    while i < len1 and j < len2:
        if inputs[1][j] == '*':
            j += 1
            if j >= len2:
                match = "true"
            while i < len1 and j < len2 and inputs[0][i] != inputs[1][j]:
                i += 1
        if j < len2 and inputs[1][j] == '\\':
            j += 1            
             
        if i < len1 and j < len2 and match_char(inputs[0], inputs[1], i, j):
            j += 1
            
        else:
            j = 0
        if j == len2:
            match = "true"
            break
        i += 1         
    
    sys.stdout.write(match)
    pass

test_cases.close()
