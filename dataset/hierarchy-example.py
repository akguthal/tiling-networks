import networkx as nx
from networkx.algorithms import community
import itertools
import psycopg2 as db

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
for communities in itertools.islice(comp, k):
    print(tuple(sorted(c) for c in communities))
