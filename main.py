import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

# edge_objects = [(1, 2, 0.4), (1, 3, 1.7), (1, 4, 1.2), (2, 5, 0.3), (2, 6, 1.9), (3, 4, 0.1)]
edge_objects = [(1, 2, 0.4), (1, 3, 0.7), (2, 4, 0.2), (3, 4, 0.3),
                (4, 5, 0.1), (2, 5, 1.2),
                (5, 6, 1.9), (6, 7, 0.6), (3, 8, 0.6)]
start_node = [1]
end_nodes = [7, 8]
common_nodes = [2, 3, 4, 5, 6]

for from_loc, to_loc, load in edge_objects:
    G.add_edge(from_loc, to_loc, load=load)

colors = ['r', 'y']
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
edge_labels = nx.get_edge_attributes(G, 'load')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_nodes(G, pos, nodelist=start_node, node_color='b')
nx.draw_networkx_nodes(G, pos, nodelist=end_nodes, node_color='r')
nx.draw_networkx_nodes(G, pos, nodelist=common_nodes, node_color='g')

for end_node in end_nodes:
    path = nx.dijkstra_path(G, start_node[0], end_node, weight='load')
    print(path)
    path_edges = []
    end_node_index = end_nodes.index(end_node)
    for node in path:
        cur_index = path.index(node)
        next_index = path.index(node) + 1
        if len(path) > next_index:
            obj = (node, path[next_index])
            path_edges.append(obj)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color=colors[end_node_index])

plt.show()
