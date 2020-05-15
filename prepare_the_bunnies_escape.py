'''
Challenge 3.1
Prepare the Bunnies' Escape
===========================
You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 
You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 
Write a function answer(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
Output:
    (int) 7
Inputs:
    (int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
Output:
    (int) 11
    
'''

import heapq
from dataclasses import dataclass
@dataclass
class walli:
    i:int=-1
    j:int=-1
    f:int=-1
    g:int=-1
    h:int=-1

def solution(map):
    #strategy: calculate distances to all the reachable points from start and do the same from dest without breaking. Then start comparing 
    #dist calculated using both ways and keep the min one. Both ways dist will be >=1 only if that cell is reachable, so we get a 1
    # where we add dist calculated both ways. Return min such value
    ht=len(map)
    wt= len(map[0])
    #matrix= [ [ walli for j in range(3) ] for i in range(3) ]
    matrix= [ [ None for j in range(wt) ] for i in range(ht) ]
    matrix[0][0]=1
    queue=[(0,0)]
    while(len(queue)!=0):
        cord=queue.pop(0)
        #print(cord)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          successor = cord[0] + i[0], cord[1] + i[1]
          if  successor[0]>=0 and successor[0] < ht and successor[1]>=0 and successor[1] < wt:
            if matrix[successor[0]][successor[1]] is None:
                matrix[successor[0]][successor[1]] = matrix[cord[0]][cord[1]] + 1
                if map[successor[0]][successor[1]] == 1 :
                  continue
                queue.append((successor[0], successor[1]))
    #print(matrix)
    matrix2= [ [ None for j in range(wt) ] for i in range(ht) ]
    matrix2[ht-1][wt-1]=1
    queue2=[(ht-1,wt-1)]
    while(len(queue2)!=0):
        cord=queue2.pop(0)
        #print(cord)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          successor = cord[0] + i[0], cord[1] + i[1]
          if successor[0]>=0 and successor[0] < ht and successor[1]>=0 and successor[1] < wt:
            if matrix2[successor[0]][successor[1]] is None:
                matrix2[successor[0]][successor[1]] = matrix2[cord[0]][cord[1]] + 1
                if map[successor[0]][successor[1]] == 1 :
                  continue
                queue2.append((successor[0], successor[1]))
    #print(matrix2)
    ans=10000000
    for i in range(ht):
        for j in range(wt):
            if(matrix[i][j] and matrix2[i][j]):
               ans= min(matrix[i][j]+matrix2[i][j]-1,ans)
    return ans
    


print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))