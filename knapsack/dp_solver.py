##### Dynamic Programming Solver #####
# Has complexity = item_count * capacity
#Import modules
from collections import namedtuple


Item = namedtuple("Item", ['index', 'value', 'weight'])

# Implement dynamic programming solution


def solve_it(input_data):
# parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    taken = [0]*len(items)

    #initiate value and keep array

    value_array = [[0 for j in range(capacity)]for i in range(item_count +1)]
    keep_array = [[0 for j in range(capacity)]for i in range(item_count +1)]
    weights = range(1,capacity+1)

    #Implement dynamic programming solution
    for i in range(1,item_count+1): # item column
        
        for j in range(capacity): #weight row
            # we store past values and compare current knapsack value with the value of the 
            #new item + knapsack you can get with remaining weight
            if items[i-1].weight <= weights[j] :
                remaining_weight = weights[j] - items[i-1].weight
                value_array[i][j] = max(items[i-1].value + value_array[i-1][max(remaining_weight-1,0)],value_array[i-1][j])

            else :            
                value_array[i][j] = value_array[i-1][j]

            if value_array[i][j] > value_array[i-1][j] :
                keep_array[i][j] = 1

    #now backtrack
    w = capacity 
    i = item_count 
    value = 0
    #starting from lower right, we will see which items we keep, reducing our remaining cap
    #until no more capacity is available or you've run through all items
    for i in range(item_count,0,-1) :

        if keep_array[i][w-1] == 1 and w > 0:
            taken[i-1] = 1
            w -= items[i-1].weight
            value += items[i-1].value

    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'



