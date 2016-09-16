import numpy as np

def load_graph(location):
    """ Format the graph from the provided txt file. Returns a dictionary:
    {node: [edges]}
    """
    
    with open(location, 'r') as f:

        graph = {}

        for line in f:
            line = line.split('\t')
            graph[line[0]] = line[1:-1]

    return graph


def contract_edges(graph):
    """ The recursive contraction of edges. Returns a given prospective min cut. """
    
    keys = list(graph.keys())
    # base case
    if len(keys) == 2:
        firstKey = keys[0]
        return len(graph[firstKey])

    # pick a random node
    nodeToCutFrom = keys[np.random.randint(0, len(keys))]

    # pick a random edge
    edgesFromSelectedNode = graph[nodeToCutFrom]
    edgeToCut = edgesFromSelectedNode[np.random.randint(0, len(edgesFromSelectedNode))]

    # merge along that edge:
    # a) we must merge the two nodes themselves and b) also go through all the other nodes
    # and make sure they point to the new, merged node as well

    # a) (we take the convention of removing the "edgeToCut" node)
    graph[nodeToCutFrom] += graph.pop(edgeToCut) 
    # b) replace all references to edgeToCut with nodeToCutFrom
    for node, edges in graph.items():

        # its possible that for the given node, the edge exists 0-n times
        while edgeToCut in edges:
            edges[edges.index(edgeToCut)] = nodeToCutFrom

        graph[node] = edges

    # remove self-referencing edges post merge
    graph[nodeToCutFrom] = [x for x in graph[nodeToCutFrom] if x != nodeToCutFrom]

    return contract_edges(graph)


def find_min_cut(n):
    """ The overall algorithm, in which we identify a prospective min cut n Choose 2 * log n
    times. This guarantees that the likelihood of failure to find the minimum cut is 1/n, 
    where n is the number of nodes in the graph. """
    

    itersToRun = np.ceil(n * np.log(n)) # chance of failing is 1/n now

    minCut = np.inf
    for i in range(int(itersToRun)):
        print(i)
        graph = load_graph(location)
        # change the seed
        np.random.seed(i*12)

        # update minCut
        randomCut = contract_edges(graph)
        minCut = randomCut if randomCut < minCut else minCut

    return minCut


def main():
    location = r"C:\Users\ashamlian\Downloads\mincut.txt"
    mc = find_min_cut(200)
    print(mc)

if __name__ == '__main__':
    main()