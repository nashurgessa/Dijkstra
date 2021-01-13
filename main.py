from graph import Graph
from Dijkstra import dijkstra_algo, shortest

if __name__ == "__main__":
    g = Graph()
    print("______________________ Algorithm code implementation __________ ")
    # Add the location
    g.add_vertex('Xian')
    g.add_vertex('Beijing')
    g.add_vertex('Taiyuan')
    g.add_vertex('Yulin')
    g.add_vertex('Shuozhou')
    g.add_vertex('Datong')   
    
    print("Intialized vertex: ", g.vert_dict.keys())
    # print("Check Vertex object is intialized: ", iter(g.vert_dict.values()))
    # print('If vertex A exists in the graph', str(g.get_vertex('A')))
    
    g.add_edge('Xian', 'Taiyuan', 374)  
    g.add_edge('Beijing', 'Taiyuan', 303)
    g.add_edge('Xian', 'Yulin', 789)
    g.add_edge('Yulin', 'Taiyuan', 205)
    g.add_edge('Shuozhou', 'Yulin', 300)
    g.add_edge('Shuozhou', 'Datong', 112)
    g.add_edge('Taiyuan', 'Shuozhou', 170)
    g.add_edge('Beijing', 'Shuozhou', 305)
    g.add_edge('Beijing', 'Datong', 215)
    
    print("---------------------------------------------------- Creating a Graph  -------------------------------------")
    print("Graph data")
    for v in g:
        # print(v)  # vertex
        for w in v.get_connections(): # weight    
            vid = v.get_id()
            wid = w.get_id()
            
            print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))
            
    print("--------------------------------------- Implementing the Dijkstar Algorithm ----------------------------------")
    
    starting_point = g.get_vertex('Xian') 
    
    dijkstra_algo(g, starting_point)
    
    destination_point = g.get_vertex('Beijing')
    path = [destination_point.get_id()]
    # print(path)
    shortest(destination_point, path)
    print('The shortest path : %s' %(path[::-1])) 