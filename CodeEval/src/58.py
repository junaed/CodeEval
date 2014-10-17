import sys
import Queue
from collections import defaultdict

def calculate_distance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    i = 0
    while i<len1 and i<len2:
        if word1[i] != word2[i]:
            return (word1[i+1:] == word2[i+1:]) or (word1[i+1:] == word2[i:]) or (word1[i:] == word2[i+1:])
        i+=1
    return abs(len1-len2)==1
        
# test_cases = open(sys.argv[1], 'r')
test_cases = open("58.txt", 'r')
word_dictionary = {}
words_by_length = {}
inputs = []
dictionary_started = False
i = 0
for line, test in enumerate(test_cases):
    test = test.strip()
    if test == "END OF INPUT":
        dictionary_started = True
        continue
    if dictionary_started == False:
        inputs.append(test)
    else:
        word_dictionary[test] = True
#         word_list.append(test)
        l = len(test)
        if l not in words_by_length:
            words_by_length[l] = [test]
        else:
            words_by_length[l].append(test)
    pass
test_cases.close()
 
 
wdlen = len(word_dictionary)
 
for c, ip in enumerate(inputs):
    q = Queue.Queue()
    q.put(ip)
    if ip in word_dictionary: 
        word_dictionary[ip] = False
    size = 1
#     length_checked = []
    while not q.empty():
        current_item = q.get()
        cl = len(current_item)
        
        for x in [cl - 1, cl, cl + 1]:
            if x == 0:
                continue
            if x in words_by_length:
                words = words_by_length[x]
                for w in words:
                    if word_dictionary[w] and w != current_item:
                        d = calculate_distance(current_item, w)
                        if d == 1:
                            q.put(w)
                            word_dictionary[w] = False
                            size += 1      
            
    if c > 0:
        sys.stdout.write("\n")
    sys.stdout.write(str(size))
    word_dictionary = defaultdict(lambda:True, word_dictionary) 
    pass
