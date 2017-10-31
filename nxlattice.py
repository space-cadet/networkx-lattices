import networkx as nx

class Lattice():

    graph = nx.empty_graph(0)
    size = 0
    state = np.empty([]) # create empty array
    color_map = {1:'r',-1:'b'}
    node_color_dict = {} # dictionary whose keys are nodes and values are colors for each node
    node_colors = []
    pos_dict = {}

    scale_mult = 0

    def __init__(self,size=10,periodic=False):
        self.size = size
        self.graph = nx.grid_2d_graph(size,size,periodic)
        self.state = np.zeros([size,size])
        self.setRandomState()

        self.scale_mult = 10.0/self.size

        for node in self.graph:
            self.pos_dict[node] = [self.scale_mult*node[0],self.scale_mult*node[1]] # set the node co-ordinates to be same as node indices

    def setRandomState(self):
        '''Iterates over all nodes in the graph. For each node, creates an attribute
        labeled 'state', and assigns to it +1 or -1 at random  '''
        values = [-1,1] # Possible states of a given site
        for node in self.graph:
            self.graph.node[node]['state'] = values[np.random.randint(2)]
#             self.node_color.append(self.color_map[self.graph.node[node]['state']])
#             self.node_color_dict[node] = self.color_map[self.graph.node[node]['state']]
            self.graph.node[node]['color'] = self.color_map[self.graph.node[node]['state']]
#         self.node_colors = list(self.node_color_dict.values())
        self.node_colors = list(nx.get_node_attributes(self.graph,'color').values())

    def draw(self):
        nx.draw(self.graph,pos=self.pos_dict,node_color=self.node_colors,node_size=50*self.scale_mult)
