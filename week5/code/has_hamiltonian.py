adj_list_moo = {4: [5], 6: [5], 5: [7], 7: []}

def dfs_topsort(graph):         # recursive dfs with 
    L = []                      # additional list for order of nodes
    color = { u : "white" for u in graph }
    found_cycle = [False]
    for u in graph:
        if color[u] == "white":
            dfs_visit(graph, u, color, L, found_cycle)
        if found_cycle[0]:
            break
 
    if found_cycle[0]:           # if there is a cycle, 
        L = []                   # then return an empty list  
 
    L.reverse()                  # reverse the list
    return L                     # L contains the topological sort
 
 
def dfs_visit(graph, u, color, L, found_cycle):
    if found_cycle[0]:
        return
    color[u] = "gray"
    for v in graph[u]:
        if color[v] == "gray":
            found_cycle[0] = True
            return
        if color[v] == "white":
            dfs_visit(graph, v, color, L, found_cycle)
    color[u] = "black"      # when we're done with u,
    L.append(u)             # add u to list (reverse it later!)

def has_hamiltonian(adj_list):
    graph_sorted = dfs_topsort(adj_list)  
    print(graph_sorted)
    for i in range(0, len(graph_sorted) - 1):
        cur_node = graph_sorted[i]
        next_node = graph_sorted[i + 1]
        if next_node not in adj_list[cur_node]:
            return False
    
    return True

print(has_hamiltonian(adj_list_moo))
