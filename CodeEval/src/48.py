'''
Created on Sep 23, 2014

@author: junaed
'''
import sys
from fractions import gcd

vowels = 'aeiouy'

def count_letters(test):
    test = test.lower()
    count = 0
    for c in test:
        if c >= 'a' and c <= 'z':
            count += 1
    return count

def calculate_vowels(text):
    count = 0
    text = text.lower()
    for char in text:
        if char in vowels:
            count += 1
    return count

def calculate_consonants(text):
    count = 0
    text = text.lower()
    for char in text:
        if (char not in vowels) and (char >= 'a' and char <= 'z'):
            count += 1
    return count

def compute_SS(product, customer):
    p_len = count_letters(product)
    c_len = count_letters(customer)
    SS = 0.0
    if p_len % 2 == 0:
        SS = calculate_vowels(customer) * 1.5
    else:
        SS = calculate_consonants(customer) * 1.0
        
    if gcd(p_len, c_len) > 1:
        SS *= 1.5
    return SS

def step_one(data):
    min_in_row = 0
    nrows = len(data)
    ncols = len(data[0])
    
    for i in xrange(0,nrows):
        min_in_row = min(data[i])
        for j in xrange(0,ncols):
            data[i][j] -= min_in_row
    return 2, data
    
def step_two(data):
    nrows = len(data)
    ncols = len(data[0])
    row_cover = [0] * nrows
    col_cover = [0] * ncols
    M = [[0 for x in xrange(0,nrows)] for x in xrange(0,ncols)]
    
    for i in xrange(0,nrows):
        for j in xrange(0,ncols):
            if  data[i][j] and row_cover[i] == 0 and col_cover[j] == 0:
                M[i][j] = 1
                row_cover[i] = 1
                col_cover[j] = 1
#     row_cover = 
    return 3, data, M
    

def step_three(data, M):
    nrows = len(data)
    ncols = len(data[0])
#     row_cover = [0] * nrows
    col_cover = [0] * ncols
    for i in xrange(0,nrows):
        for j in xrange(0,ncols):
            if M[i][j] == 1:
                col_cover[j] = 1
    col_count = 0
    for i in xrange(0,ncols):
        if col_cover[i] == 1:
            col_count+=1
    if col_count >= ncols or col_count >= nrows:
        return 7
    return 4

def step_four():
    

def run_munkres(step = 1, data):
    done = False
    while not done:
        if step == 1:
            step, data = step_one(data)
        elif step == 2:
            step, data, M = step_two(data)
        elif step ==3:
            step = step_three()
        elif step == 4:
            step = step_four()
        elif step == 5:
            step = step_five()
        elif step == 6:
            step = step_six()
        elif step == 7:
            step = step_seven()
            done = True

if __name__ == '__main__':
#     test_cases = open(sys.argv[1], 'r')
    test_cases =  open("48_1.txt", 'r')
    for line, test in enumerate(test_cases):
        inputs = test.strip().split(";")
        products = inputs[1].split(',')
        customers = inputs[0].split(',')
        data = []
        for i in xrange(0,len(customers)):
            row = []
            for j in xrange(0,len(products)):
                row.append(compute_SS(products[j], customers[i]))
            data.append(row)
        print data
#         max_ss = calculate_all_SS(products, customers)
#         if line > 0:
#             sys.stdout.write("\n")
#         sys.stdout.write("{0:.2f}".format(max_ss))
#         max_ss = 0
#         print p
    test_cases.close()
    
    
    
