from pandas import *
def bfs():
    x=int(input("Enter Number to be searched\n"))
    e=int(input("Enter Number of edges\n"))
    v=int(input("Enter Number of vertices\n"))
    vl= list(map(int,input("Enter list of vertex edges").split()))

    print("Enter 4 space separated integers for begining vertex, Ending Vertex , weight, 1 for bi-directed or 0 for unidirected\n")
    graph=[[0 for i in range(v)] for i in range(v)]

    for _ in range(e):
        #B - Begining vertex
        #E - Ending vertex
        #W - Weight
        #D - Direction
        B,E,W,D = map(int , input().split())
        B=vl.index(B)
        E=vl.index(E)
        graph[B][E]=W
        graph[E][B] = W if D else graph[E][B]

    print(DataFrame(graph))

    L=[0]
    visited=[0]

    if x == vl[0]:
        print("Found")
        return
    while(L != []):
        for i in range(v):
            if graph[L[0]][i] != 0 and i not in visited:
                L.append(i)
                visited.append(i)
                if x == vl[i]:
                    print("found")
                    return
        #print(L)
        L.pop(0)

    print("Not Found")


bfs()
