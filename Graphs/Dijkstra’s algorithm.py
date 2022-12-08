"""
task to find shortest root from start to finish using Dijkstra's algorithm
"""
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['fin'] = 5
graph['b']['a'] = 3
graph['fin'] = {}

infinity = float('inf')

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # iterate over all nodes
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # Find the node with the lowest cost among unprocessed

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():  # Loop through all neighbors of the current node
        new_cost = cost + neighbors[n]  # If the neighbor can be reached faster through
        if costs[n] > new_cost:  # the current node, update the cost for this node
            costs[n] = new_cost
            parents[n] = node  # This node becomes the new parent for the neighbor
    processed.append(node)  # The node is marked as processed
    print(parents)
    print(costs)
    node = find_lowest_cost_node(costs)

print(f"shortest distance from start to finish is {costs['fin']}")
