import networkx as nx
from networkx.algorithms import community
import itertools
import psycopg2 as db
import pickle
import os.path

def import_into_db(nodes_to_parents, groups_with_elements):
    conn = db.connect(user='tiling_networks_user', password='password', dbname='tiling_networks', host='127.0.0.1', port='5432')
    cursor = conn.cursor()
    cursor.execute(open("init.sql", "r").read())
    conn.commit()

    cid = 0
    lookup_cid = {}

    for key in nodes_to_parents:
        lookup_cid[key] = cid

        is_leaf = (key not in nodes_to_parents.values()) # no nodes have this node as a parent

        parent_cid = -1
        if nodes_to_parents[key] != -1:
            parent_cid = lookup_cid[nodes_to_parents[key]]

        if is_leaf:
            members = groups_with_elements[key]
            for member in members:
                query = "INSERT INTO members (mid, member, value, community) VALUES (%s, %s, %s, %s);" % (member, "'"+member+"'", 1, cid)
                cursor.execute(query)


        entry = (cid, len(groups_with_elements[key]), parent_cid, is_leaf)
        query = "INSERT INTO communities (cid, sum, parent, leaf) VALUES (%s);" % ', '.join(map(str,entry))
        cursor.execute(query)

        cid += 1

    conn.commit()

def run_gn():
    f = open("email-Eu-core.txt","r")
    o = open("email-Eu-core-short.txt","w")
    for _ in range(2000) : # take subset of large network
        lineout = f.readline()
        o.write(lineout)
    G = nx.read_adjlist("./email-Eu-core-short.txt")
    print("graph assembled")
    print("number of nodes:",nx.number_of_nodes(G))
    print("number of edges:",nx.number_of_edges(G))

    comp = community.girvan_newman(G)
    k = 10
    gn_iterations = []
    iteration = {}    

    for iteration in itertools.islice(comp, k):
        gn_iterations.append(tuple(sorted(c) for c in iteration))

    file = open('gn.txt', 'wb')
    pickle.dump(gn_iterations, file)
    file.close()

    return gn_iterations    


if os.path.isfile('gn.txt'):
    file = open('gn.txt', 'rb')
    gn_iterations = pickle.load(file)
    file.close()
else:
    gn_iterations = run_gn()

all_groups_to_parent = {} # map each group (node in tree) to its parent
all_groups_to_elements = {}
group_ids_prev_iteration = []
for i in range(0, len(gn_iterations), 2):
    gn_iteration = gn_iterations[i]
    group_ids_this_iteration = []
    for group in gn_iteration:
        group_id = (group[0], len(group)) # identify each node in our tree uniquely by (first_element, size)
        group_ids_this_iteration.append(group_id) # keep track of all groups looked at this iteration
        all_groups_to_elements[group_id] = group

        if group_id not in all_groups_to_parent:

            all_groups_to_elements[group_id] = group

            if i == 0: # root
                all_groups_to_parent[group_id] = -1

            # search the last iteration's groups to find the parent (just check the first element in the group)
            for group_to_check in group_ids_prev_iteration:
                if group[0] in all_groups_to_elements[group_to_check]:
                    parent_id = group_to_check
                    all_groups_to_parent[group_id] = parent_id
                    break

    group_ids_prev_iteration = group_ids_this_iteration


import_into_db(all_groups_to_parent, all_groups_to_elements)

