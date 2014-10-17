import sys

test_cases = open(sys.argv[1], 'r')
# test_cases = open("32.txt", 'r')
for line, test in enumerate(test_cases):
    if len(test.strip("\n"))==0:
        continue
    test_strings = str(test).split(",")
    
    len_1 = len(test_strings[0])
    len_2 = len(test_strings[1].strip("\n"))
    
    if len_1 < len_2:
        sys.stdout.write("0\n")
        continue
#     sys.stdout.write(test_strings[0][(len_1-len_2+1):])
#     sys.stdout.write(test_strings[1])
    a = str(test_strings[0][(len_1-len_2):])
    b =  str(test_strings[1]).strip("\n")
    if line > 0:
        sys.stdout.write("\n")
    if  a.lower() == b.lower():
        sys.stdout.write("1")
        continue
    else:
        sys.stdout.write("0")
        continue
    pass

test_cases.close()