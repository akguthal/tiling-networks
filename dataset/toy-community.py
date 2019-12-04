import networkx as nx
from networkx.algorithms import community
import itertools
import csv

G = nx.read_adjlist("./adjacency-demo.txt")

k = 4
comp = community.girvan_newman(G)
limited = itertools.takewhile(lambda c: len(c) <= k, comp)
for communities in limited:
    community_list = tuple(sorted(c) for c in communities)

value_dictionary = {
    'a'   : 10,
    'b'   : 25,
    'c'   : 30,
    'd'   : 10,
    'e'   : 20,
    'i'   : 5,
    'ii'  : 2,
    'iii' : 3,
    'iv'  : 4,
    'v'   : 9,
    '1'   : 10,
    '2'   : 15,
    '3'   : 20,
    '4'   : 25,
    '5'   : 5
}

community_dict = {}
for i in range(len(community_list)) :
    comm_aggregate = 0 # we're going to aggregate sums as an example
    for member in community_list[i] :
        comm_aggregate += value_dictionary[member]

    community_dict[i+1] = [comm_aggregate, 0]

total_sum = 0
for entry in community_dict :
    total_sum += community_dict[entry][0]

community_dict[0] = [total_sum, -1]
print(community_dict)

with open('community-sql.csv',mode='w') as file :
    output = csv.writer(file)

    # we want two tables: one with our aggregates and one with our original data. this is the aggregates - so we just need the communities and their sums
    for key in community_dict :
        # writes the key, the summed value, and the parent
        output.writerow([key, community_dict[key][0], community_dict[key][1]])

with open('individual-sql.csv',mode='w') as file :
    output = csv.writer(file)

    # this table has the actual entries. I imagine we can JOIN these tables later.
    for i in range(len(community_list)) :
        curr_tuple = community_list[i]
        for entry in curr_tuple :
            output.writerow([entry, value_dictionary[entry], i])
