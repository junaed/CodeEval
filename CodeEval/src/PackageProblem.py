'''
Created on Sep 25, 2014

@author: junaed
'''

import sys

def get_current_cost_weight(combination, weight, cost):
    ccost = 0
    cweight = 0
    for i in xrange(len(combination)):
        if combination[i]:
            ccost += cost[i]
            cweight += weight[i]
    return ccost, cweight

def recursive_knapsack(weight_limit, weight, cost, so_far_cost, so_far_weight, so_far_combination, current_combination=None):
    
    if current_combination == None:
        current_combination = []
    if len(current_combination) == len(weight):
        m_cost, m_weight = get_current_cost_weight(current_combination, weight, cost)
        
        if m_weight < weight_limit and (m_cost > so_far_cost or (m_cost == so_far_cost and m_weight < so_far_weight)):
            return m_cost, m_weight, current_combination
        else:
            return so_far_cost, so_far_weight, so_far_combination

    so_far_cost, so_far_weight, so_far_combination = recursive_knapsack(weight_limit, weight, cost, so_far_cost, so_far_weight, so_far_combination, current_combination + [False])
    so_far_cost, so_far_weight, so_far_combination = recursive_knapsack(weight_limit, weight, cost, so_far_cost, so_far_weight, so_far_combination, current_combination + [True])

    return so_far_cost, so_far_weight, so_far_combination


def knapsack(limit, weight, cost, index):
#     print limit, weight
    start = 0
    n = len(index)
    K = [[{"cost":0, "weight":0, "keep":False} for x in xrange(start, limit + 1)] for y in xrange(0, n + 1)]
    for i in xrange(0, n + 1):
        for w in xrange(start, limit + 1):
            w -= start
            if i == 0 or w == 0:
                continue
            else:
                cost_without_item_i = (K[i - 1][w])["cost"]
                if weight[i - 1] <= w:
                    current_item_cost = cost[i - 1] + ((K[i - 1][w - weight[i - 1]])["cost"])
                    new_weight = weight[i - 1] + (K[i - 1][w - weight[i - 1]])["weight"]
                    
                    if current_item_cost > cost_without_item_i:                    
                        (K[i][w])["cost"] = current_item_cost
                        (K[i][w])["weight"] = new_weight
                        (K[i][w])["keep"] = True
                    
                    elif current_item_cost == cost_without_item_i:
                        if (K[i - 1][w])["weight"] > new_weight:
                            (K[i][w])["cost"] = current_item_cost
                            (K[i][w])["weight"] = new_weight
                            (K[i][w])["keep"] = True
                        else:
                            (K[i][w])["cost"] = (K[i - 1][w])["cost"]
                            (K[i][w])["weight"] = (K[i - 1][w])["weight"] 
                    else:
                        (K[i][w])["cost"] = (K[i - 1][w])["cost"]
                        (K[i][w])["weight"] = (K[i - 1][w])["weight"]
                else:
                    (K[i][w])["cost"] = (K[i - 1][w])["cost"]
                    (K[i][w])["weight"] = (K[i - 1][w])["weight"]
    bag = []
    line = limit-start
    i = n
    while i > 0:
        if (K[i][line])["keep"]:
            bag.append(index[i - 1])
            line -= weight[i - 1]
        i -= 1
    if len(bag) == 0:
            sys.stdout.write("-")
    else:
        for j, a in enumerate(sorted(bag)):
            if j > 0:
                sys.stdout.write(",")
            sys.stdout.write(str(a))

if __name__ == '__main__':
    test_cases =  open(sys.argv[1], 'r')
#     test_cases = open("package_large.txt", 'r')
    
    multiplier = 100
    for l, test in enumerate(test_cases):
        index = []
        weight = []
        cost = []
        test = test.strip("\n")
        test = test.strip()
        if len(test) == 0:
            continue
        tests = test.split(":")
        limit = int(tests[0].strip()) * multiplier
        
        rest = tests[1].strip().split(" ")
        for item in rest:
            item = item.strip()
            item = item.strip("()")
            items = item.split(",")
            index.append(int(items[0]))
            weight.append(int(float(items[1]) * multiplier))
            cost.append(float(items[2].strip("$")))
        if l > 0:
            sys.stdout.write("\n")
        c_cost, c_weight, c_used = recursive_knapsack(limit, weight, cost, 0, limit+100.0, [], [])
#         gc.collect()
        result = []
        for i in xrange(len(c_used)):
            if c_used[i]: result.append(index[i])
        if len(result) == 0:
            sys.stdout.write('-')
        else:
            sys.stdout.write(','.join([str(x) for x in sorted(result)]))
                
    test_cases.close()
    pass
