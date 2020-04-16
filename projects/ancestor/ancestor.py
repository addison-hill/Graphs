from graph import Graph
from util import Stack, Queue

# Transfer to graph terminology
# Build your graph
# Traverse your graph

# Since the graph is unidirectional you can flip the edges by flipping the values in the tuple
# Then we can use BFS to find earliest ancestor from child

# do BFS, store the path, and return the path with the longest value

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# new = [(3, 1), (3, 2), (6, 3), (6, 5), (7, 5), (5, 4), (8, 4), (9, 8), (8, 11), (1, 10)]
"""
  10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
"""


# def earliest_ancestor(ancestors, starting_node):
#     # build graph
#     gg = Graph()
#     # initialize vertices and edges
#     # we need to get rid of duplicates to enter our vertices in
#     ll = []
#     for i in ancestors:
#         # this is each tuple
#         for j in i:
#             if j not in ll:
#                 ll.append(j)

#     for vert in ll:
#         gg.add_vertex(vert)

#     # initialize edges but flip values
#     for edge in ancestors:
#         gg.add_edge(edge[1], edge[0])

#     print(ll)
#     print(gg.vertices)

#     # now we have graph set up, we need to use BFT to find ancestor
#     qq = Queue()
#     qq.enqueue([starting_node])
#     visited = set()
#     while qq.size() > 0:
#         path = qq.dequeue()
#         if path[-1] not in visited:
#             visited.add(path[-1])
#             if gg.get_neighbors(path[-1]):
#                 for neighbor in gg.get_neighbors(path[-1]):
#                     new_path = path.copy()
#                     new_path.append(neighbor)
#                     qq.enqueue(new_path)
#             elif path[-1] == starting_node:
#                 return -1
#             else:
#                 return path[-1]

# (parent, child)

def get_parents(ancestors, child):
    results = list()
    for item in ancestors:
        if child == item[1]:
            results.append(item[0])
    return results


def earliest_ancestor(ancestors, starting_node):
    # make a set of children
    child_list = set()
    for item in ancestors:
        child_list.add(item[1])
    # if starting node doesn't have a parent return -1
    if starting_node not in child_list:
        return -1
    else:
        # make an empty stack
        s = Stack()
        # push the starting node into the stack
        s.push([starting_node])
        # keep track of which nodes you've visited
        visited = set()
        # while there is something in the stack
        while s.size() > 0:
            # remove the first item from the stack
            path = s.pop()
            # remove the first item from the path
            n = path[-1]
            # check if n has been visited
            if n not in visited:
                # if not... add it to the visited set
                visited.add(n)
            # get a list of parents for the current node
            for parent in get_parents(ancestors, n):
                # make a copy of the path
                path_copy = path.copy()
                # append that parent node to the path_copy
                path_copy.append(parent)
                # push the path copy into the stack
                s.push(path_copy)
                # print(path)
                # print(parent)
        # return earliest ancestor
        return path[-1]


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print(earliest_ancestor(ancestors, 1))  # 10
# print(earliest_ancestor(ancestors, 2))  # -1
# print(earliest_ancestor(ancestors, 3))  # 10
# print(earliest_ancestor(ancestors, 11))  # -1
# print(earliest_ancestor(ancestors, 5))  # 4
# print(earliest_ancestor(ancestors, 7))  # 4
# print(earliest_ancestor(ancestors, 8))  # 4
# print(earliest_ancestor(ancestors, 9))  # 4

# earliest_ancestor(ancestors, 9)

# Alexs solution!!

# def earliest_ancestor(ancestors, starting_vertex):
#   graph = {}
#   for ancestor in ancestors:
#     if ancestor[0] not in graph:
#       graph[ancestor[0]] = set()
#     if ancestor[1] not in graph:
#       graph[ancestor[1]] = set()
#     # add nodes in reverse order
#     graph[ancestor[1]].add(ancestor[0])
#   stack = []
#   visited = set()
#   stack.append(starting_vertex)
#   while len(stack) > 0:
#     current = stack.pop()
#     if current not in visited:
#       visited.add(current)
#       neighbors = graph[current]
#       if len(neighbors) > 0:
#         sorted_neighbors = sorted(neighbors)
#         for neighbor in sorted_neighbors:
#           stack.append(neighbor)
#       if len(stack) == 0:
#         return current
#   return -1
