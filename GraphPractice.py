import decimal as d


class GraphPractice(object):


    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.__graphDict = graph_dict

    def has_edge(self, key, value):
        list_of_values = self.__graphDict[key]
        if key in self.__graphDict and value in list_of_values:
            print("edge exists")
        else:
            print("edge does not exist")

    def add_edge(self, vertex1, vertex2):
        list_of_values = self.__graphDict[vertex1]
        if vertex2 in list_of_values:
            print("edge already exists")
        else:
            self.__graphDict[vertex1].append(vertex2)
            print("edge successfully added")

    def delete_edge(self, key, value):
        list_of_values = self.__graphDict[key]
        if key in self.__graphDict and value in list_of_values:
            self.__graphDict[key].remove(value)
            print("edge removed")

    def add_vertex(self, vertex):
        if vertex in self.__graphDict:
            print("vertex already exists")
        if vertex not in self.__graphDict:
            self.__graphDict[vertex] = []
            print("added node: " + vertex + " to graph")

    def delete_vertex(self, vertex):
        if vertex not in self.__graphDict:
             print("vertex does not exist")
        if vertex in self.__graphDict:
            del self.__graphDict[vertex]
            print("vertex removed")



    def graph_density(self):
        num_vert = self.count_vertices()
        num_edge = self.count_edges()
        max_edges = num_vert * (num_vert -1)
        density = num_edge / max_edges
        return density

    def is_sparse(self):
        density = self.graph_density()
        if density <= .15:
            print("graph is sparse")
            return
        else:
            print("graph is not sparse")

    def is_dense(self):
        density = self.graph_density()
        if density >= .85:
            print("graph is dense")
            return
        else:
            print("graph is not dense")


    def count_vertices(self):
        count = len(self.__graphDict)
        return count

    def count_edges(self):
        ctr = sum(map(len, self.__graphDict.values()))
        return ctr

def main():
    g = {}
    graph = GraphPractice(g)
    print(g)
    graph.add_vertex("a")
    graph.add_vertex("b")
    graph.add_vertex("c")
    graph.add_vertex("d")
    graph.add_vertex("e")
    graph.add_vertex("f")
    graph.add_edge("a", "e")
    graph.add_edge("a", "b")
    print(g)
    graph.delete_vertex("f")
    print(g)
    graph.graph_density
    graph.is_sparse()
    graph.is_dense()
    graph.add_edge("a", "c")
    graph.add_edge("a", "d")
    graph.add_edge("e", "a")
    graph.add_edge("b", "c")
    graph.add_edge("b", "d")
    graph.add_edge("b", "a")
    graph.add_edge("b", "e")
    graph.add_edge("d", "a")
    graph.add_edge("d", "b")
    graph.add_edge("d", "c")
    graph.add_edge("d", "e")
    graph.add_edge("d", "f")
    graph.add_edge("e", "b")
    graph.add_edge("e", "c")
    graph.add_edge("e", "d")
    graph.is_dense()
    print(g)


main()





   # def isDense(self):   num edges ~= vertex^2
  #  def isConnected(self):
  #   def isFullyConnected(self):
  #  def readGraph(self):
  #  def printGraph(self)




