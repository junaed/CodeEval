'''
Created on Sep 23, 2014

@author: junaed
'''
import sys
from fractions import gcd
from itertools import permutations

vowels = 'aeiouy'

def count_letters(test):
    test = test.lower()
    count = 0
    for c in test:
        if c >='a' and c<='z':
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
        if (char not in vowels) and (char >='a' and char <='z'):
            count += 1
    return count

def compute_SS(product, customer):
    p_len = count_letters(product)
    c_len = count_letters(customer)
    SS = 0
    if p_len %2 == 0:
        SS = calculate_vowels(customer) * 1.5
    else:
        SS = calculate_consonants(customer)
        
    if gcd(p_len, c_len) > 1:
        SS *= 1.5
    return SS

def calculate_all_SS_memory(products, customers):
    SS_dict = {}
    for customer in customers:
        all_ss = {}
        for product in products:
            ss = compute_SS(product, customer)
            all_ss[product] = ss
        SS_dict[customer] = all_ss
    if len(customers) <= len(products):
        data = [i for i in xrange(0,len(products))]
    else:
        data = [i for i in xrange(len(products)-len(customers),len(products))]
    perms = list(permutations(data,len(customers)))
    max_ss = 0
    maxp = None
    for row in perms:
        ss = 0.0
        for i,v in enumerate(row):
            if v >= 0:
#                 print i, customers[i]
                cus_data = SS_dict[customers[i]]
                ss += cus_data[products[int(v)]]
        if max_ss < ss:
            max_ss = ss
            maxp = row
    return max_ss, maxp        
    
def calculate_all_SS(products, customers):
    SS_dict = {}
    for customer in customers:
        all_ss = {}
        for product in products:
            ss = compute_SS(product, customer)
            all_ss[product] = ss
        SS_dict[customer] = all_ss
    if len(customers) <= len(products):
        data = [i for i in xrange(0,len(products))]
    else:
        data = [i for i in xrange(len(products)-len(customers),len(products))]
    
    max_ss = 0.0
    maxp = None
    
    for perms in permutations(data,len(customers)):
        row = list(perms)
#         print row
        ss = 0.0
        for i,v in enumerate(row):
            if v >= 0:
#                 print i, customers[i]
                cus_data = SS_dict[customers[i]]
                ss += cus_data[products[int(v)]]
        if max_ss < ss:
            max_ss = ss
            maxp = row
    return max_ss,maxp  

if __name__ == '__main__':
#     test_cases =  open(sys.argv[1], 'r')
    test_cases =  open("48_1.txt", 'r')
    for line, test in enumerate(test_cases):
        inputs = test.strip().split(";")
        products = inputs[1].split(',')
        customers = inputs[0].split(',')
        max_ss, p= calculate_all_SS(products, customers)
        if line>0:
            sys.stdout.write("\n")
        sys.stdout.write("{0:.2f}".format(max_ss))
        print p
    test_cases.close()
    
    
    