import networkx as nx
from networkx.algorithms import community
import itertools
import psycopg2 as db

def minLength(list) :
    minLength = None
    for sublist in list:
        if minLength == None:
            minLength = len(sublist)
        elif len(sublist) < minLength :
            minLength = len(sublist)
    return minLength

# INITIALIZE TABLES
# conn = db.connect(user='tiling_networks_user', password='password', dbname='tiling_networks', host='127.0.0.1', port='5432')
# cursor = conn.cursor()
# cursor.execute(open("init.sql", "r").read())
# conn.commit()

# GENERATE DUMMY DATA
G = nx.read_adjlist("./hierarchy.txt")

k = 3
comp = community.girvan_newman(G)
# limited = itertools.takewhile(lambda c: len(c) <= k, comp)
# for communities in limited:
#     community_list = tuple(sorted(c) for c in communities)
# for communities in itertools.islice(comp, k):
#     print(tuple(sorted(c) for c in communities))

done = False
niters = 0
prev_list = None
while not done:
    niters += 1
    curr_list = tuple(sorted(c) for c in next(comp))
    current_min = minLength(curr_list)
    print(current_min)
    print(current_list)
    if current_min == 1 :
        done = True
