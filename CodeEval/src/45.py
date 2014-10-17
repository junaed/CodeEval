'''
Created on Sep 22, 2014

@author: junaed
'''

import sys

def reverse(n):
    if n < 10:
        return n
    org = n
    new = 0
    while n > 0:
        new = (new * 10) + (n % 10)
        n = n / 10
    return new
        
def palindrom_check(n):
    if n == reverse(n):
        return True
    return False

def main_function():
    test_cases = open(sys.argv[1], 'r')
#     test_cases = open("45.txt", 'r')
    for line, test in enumerate(test_cases):
        test = int(test.strip())
        it = 0
        while not palindrom_check(test):
            it +=1
            rev = reverse(test)
            test += rev
            if it == 100:
                break
        if line > 0:
            sys.stdout.write("\n")
        sys.stdout.write("{} {}".format(it,test))
    test_cases.close()


if __name__ == '__main__':
    main_function()
#     print palindrom_check(12321)
#     print palindrom_check(12121)
#     print palindrom_check(12345)