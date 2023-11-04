#   Created by Elshad Karimov 
#   Copyright © 2023 AppMillers. All rights reserved.
import queue
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    def bfs(self,vertex):
        visited = set()
        que=queue.Queue()
        que.put(vertex)
        visited.add(vertex)
        while not que.empty():
            cur_vertex=que.get()
            print(cur_vertex)
            for adj_vertex in self.adjacency_list[cur_vertex]:
                if adj_vertex not in visited:
                    visited.add(adj_vertex)
                    que.put(adj_vertex)
    def dfs(self,vertex):
        visited = set()
        sta=queue.LifoQueue()
        sta.put(vertex)
        while not sta.empty():
            cur_vertex = sta.get()
            if cur_vertex not in visited:
                print(cur_vertex)
                visited.add(cur_vertex)
            for adj_vertex in self.adjacency_list[cur_vertex]:
                if adj_vertex not in visited :
                    sta.put(adj_vertex)
    
       







my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "B")
# my_graph.add_edge("A", "D")
my_graph.add_edge("B", "E")
my_graph.add_edge("C", "D")
my_graph.add_edge("D", "E")
my_graph.print_graph()
print("bfs")
my_graph.bfs('A')
print("dfs")
my_graph.dfs('A')

  
    


