import Queue
import sys

'''
Created on Feb 7, 2015

@author: junaed
'''

def next_neighbor(x, y, index):
    if(index == 0):
        return (x + 1, y);
    elif(index == 1):
        return (x, y + 1);
    elif(index == 2):
        return (x - 1, y);
    else:
        return (x, y - 1); 

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s

def check_neighbor(x,y):
    sum_x = sum_digits(abs(x))
    sum_y = sum_digits(abs(y))
    return (sum_x+sum_y)<=19 

def dfs(start_x, start_y):
    q = Queue.Queue()
    visited = set()
    q.put((start_x,start_y))
#     node_count = 0
    while not q.empty():
        current_node = q.get()
        if current_node not in visited:
#             print current_node
            visited.add(current_node)
            current_x = current_node[0]
            current_y = current_node[1]
            for i in xrange(0,4):
                neighbor = next_neighbor(current_x, current_y, i)
                if check_neighbor(neighbor[0], neighbor[1]) and neighbor not in visited:
                    q.put(neighbor)
            
    return len(visited)

if __name__ == '__main__':
    count = dfs(0, 0)
    sys.stdout.write(str(count))
