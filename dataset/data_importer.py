import networkx as nx
from networkx.algorithms import community
import itertools
import psycopg2 as db

# INITIALIZE TABLES
conn = db.connect(user='tiling_networks_user', password='password', dbname='tiling_networks', host='127.0.0.1', port='5432')
cursor = conn.cursor()
cursor.execute(open("init.sql", "r").read())
conn.commit()

# GENERATE DUMMY DATA
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

    community_dict[i+1] = (i+1, comm_aggregate, 0, True)

total_sum = 0
for entry in community_dict :
    total_sum += community_dict[entry][1]

community_dict[0] = (0, total_sum, -1, False)


# INSERT DATA INTO THE DATABASE

# table for communities
for c in community_dict.items() :
    item = ', '.join(map(str,c[1]))
    query = "INSERT INTO communities (cid, sum, parent, leaf) VALUES (%s);" % item
    cursor.execute(query)

# table for members
mid = 0
for i in range(len(community_list)):
    c = community_list[i]
    for entry in c:
        member = (mid, entry, value_dictionary[entry], i+1)
        query = "INSERT INTO members (mid, member, value, community) VALUES (%s, %s, %s, %s);" % (member[0], "'"+member[1]+"'", member[2], member[3])
        cursor.execute(query)
        mid = mid + 1

conn.commit()
