#   N Missionaries and N Cannibals with boat capacity X

C=int(input())
M=C
boat=int(input())
if M+C<boat:
    print("Invalid Input")
    exit()
q=[[M,C,0]]
s=[[M,C,0]]
count=0
while len(q)>0:
    size=len(q)
    flag=0
    for _ in range(size):
        
        m=q[0][0]
        c=q[0][1]
        state=q[0][2]
        q.pop(0)
        if m==M and c==C and state==1:
            flag=1
            break
        if state==0:
            i=0
            j=0
            while i<=boat:
                while j<=boat:
                    if i>0 or j>0:
                        if i+j<=boat and i>=j and m-i>=c-j and m>=i and c>=j and [m-i,c-j,1] not in s:
                            q.append([m-i,c-j,1])
                            s.append([m-i,c-j,1])
                    j=j+1
                j=0
                i=i+1
        else:
            i=0
            j=0
            while i<=boat:
                while j<=boat:
                    if i>0 or j>0:
                        if i+j<=boat and i>=j and m+i>=c+j and m+i<=M and c+j<=C and [m+i,c+j,0] not in s:
                            q.append([m+i,c+j,0])
                            s.append([m+i,c+j,0])
                    j=j+1
                j=0
                i=i+1
    count=count+1
    print([m,c,state])
    if flag==1:
        break
print(count)




------------------------------------------------------------------------------------------------------------------





## Water jug problem for 2 jugs and target capacity

q = [0]
jug1Capacity=int(input("Enter capacity of jug 1 : "))
jug2Capacity=int(input("Enter capacity of jug 2 : "))
targetCapacity=int(input("Enter the target capacity : "))
total = jug1Capacity + jug2Capacity

s = [0]
cnt = 0
flag=0
while len(q) > 0:
    size = len(q)
    cnt = cnt + 1
    for _ in range(size):
        node = q.pop(0)
        if node == targetCapacity:
            flag=1
            break
        if node + jug1Capacity <= total and node + jug1Capacity not in s:
            s.append(node + jug1Capacity)
            q.append(node + jug1Capacity)

        if node + jug2Capacity <= total and node + jug2Capacity not in s:
            s.append(node + jug2Capacity)
            q.append(node + jug2Capacity)

        if node - jug1Capacity >= 0 and node - jug1Capacity not in s:
            s.append(node - jug1Capacity)
            q.append(node - jug1Capacity)

        if node - jug2Capacity >= 0 and node - jug2Capacity not in s:
            s.append(node - jug2Capacity)
            q.append(node - jug2Capacity)
    if flag==1:
        break
if flag==0:
    print("No solution")
else:
    print("Answer : ")
    print(cnt)





------------------------------------------------------------------------------------------------------------------




#8 puzzle using heuristic search


import copy

board=[[1,2,3],[5,6,0],[7,8,4]]
q=[[[1,2,3],[5,6,0],[7,8,4]]]
s=[[[1,2,3],[5,6,0],[7,8,4]]]
count=0
res=[[1,2,3],[5,8,6],[0,7,4]]
flag=0
while len(q)>0:
    size=len(q)
    for _ in range(size):
        v=q.pop(0)
        if v==res:
            flag=1
            break
        x=0
        y=0
        for i in range(3):
            for j in range(3):
                if v[i][j]==0:
                    x=i
                    y=j
                    break
        if x-1>=0 and y>=0:
            temp = copy.deepcopy(v)
            temp[x][y],temp[x-1][y]=temp[x-1][y],temp[x][y]
            if temp not in s:
                q.append(temp)
                s.append(temp)
        if x>=0 and y-1>=0:
            temp = copy.deepcopy(v)
            temp[x][y],temp[x][y-1]=temp[x][y-1],v[x][y]
            if temp not in s:
                q.append(temp)
                s.append(temp)
        if x+1<3 and y>=0:
            temp = copy.deepcopy(v)
            temp[x][y],temp[x+1][y]=temp[x+1][y],temp[x][y]
            if temp not in s:
                q.append(temp)
                s.append(temp)
        if x>=0 and y+1<3:
            temp = copy.deepcopy(v)
            temp[x][y],temp[x][y+1]=temp[x][y+1],temp[x][y]
            if temp not in s:
                q.append(temp)
                s.append(temp)
    count=count+1
    if flag==1:
        break
if flag==0:
    print("No Solution")
else:
    print("Answer : ")
    print(count-1)








------------------------------------------------------------------------------------------------------------------






##8 queens using hill hill_climbing

import random

def hit_count(board,n):
    count=0
    x=0
    y=0
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                x=i+1;
                y=j;
                while x<n: 
                    if board[x][y]==1:
                        count=count+1
                    x=x+1
                x=i-1
                while x>=0:
                    if board[x][y]==1:
                        count=count+1
                    x=x-1
                x=i
                y=j+1
                while y<n:
                    if board[x][y]==1:
                        count=count+1
                    y=y+1
                y=j-1
                while y>=0:
                    if board[x][y]==1:
                        count=count+1
                    y=y-1
                x=i-1
                y=j-1
                while x>=0 and y>=0:
                    if board[x][y]==1:
                        count=count+1
                    x=x-1
                    y=y-1
                x=i+1
                y=j-1
                while x<n and y>=0:
                    if board[x][y]==1:
                        count=count+1
                    x=x+1
                    y=y-1
                x=i+1
                y=j+1
                while x<n and y<n:
                    if board[x][y]==1:
                        count=count+1;
                    x=x+1
                    y=y+1
                x=i-1
                y=j+1
                while x>=0 and y<n:
                    if board[x][y]==1:
                        count=count+1
                    x=x-1
                    y=y+1
    return count
    
def create_new_state(n):
    board=[]
    for i in range(n):
        v=[]
        x=random.randint(0,n-1)
        for j in range(n):
            if j==x:
                v.append(1)
            else:
                v.append(0)
        board.append(v)
    return board

def compare_states(ne,curr,n):
    if hit_count(ne,n)<hit_count(curr,n):
        return ne
    return curr

def hill_climbing(curr,n):
    while hit_count(curr,n)!=0:
        ne=create_new_state(n)
        curr=compare_states(ne,curr,n)
    return curr
    
if __name__=='__main__':
    n=int(input("Enter the size of the chess board : "))
    curr=create_new_state(n)
    res=hill_climbing(curr,n)
    print("Answer :- ")
    for i in range(n):
        print(res[i])





------------------------------------------------------------------------------------------------------------------






##wumpus world

dirx = [1,-1,0,0]
diry = [0,0,1,-1]
dirt = ["Go Down", "Go Up", "Go Right", "Go Left"]
 
def create_grid():
    grid = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append('_')
        grid.append(row)
    grid[0][0] = 'P1'
    for i in range(3):
        x = int(input("Enter x-ordinate of pit: "))
        y = int(input("Enter y-ordinate of pit: "))
        grid[x][y] = 'P'
        for j in range(4):
            x = x+dirx[j]
            y = y+diry[j]
            if x>=0 and x<4 and y>=0 and y<4 and grid[x][y]=='_':
                grid[x][y] = 'B'
    x = int(input("Enter x-ordinate of Wumpus: "))
    y = int(input("Enter y-ordinate of Wumpus: "))
    grid[x][y] = 'W'
    for j in range(4):
        x = x+dirx[j]
        y = y+diry[j]
        if x>=0 and x<4 and y>=0 and y<4 and grid[x][y]=='_':
            grid[x][y] = 'S'
    x = int(input("Enter x-ordinate of Gold: "))
    y = int(input("Enter y-ordinate of Gold: "))
    grid[x][y] = 'G'
    return grid
 
def dfs(grid,vis,x,y,path):
    if(grid[x][y] == 'G'):
        return True
    if(grid[x][y] == 'W'):
        temp = path.pop()
        path.append("Shoot Arrow")
        path.append(temp)
    if(grid[x][y] == 'P'):
        return False
    for j in range(4):
        x = x+dirx[j]
        y = y+diry[j]
        if x>=0 and x<4 and y>=0 and y<4 and (x,y) not in vis:
            path.append(dirt[j])
            vis.append((x,y))
            if(dfs(grid,vis,x,y,path)):
                return True
            temp = path.pop()
            if temp == "Shoot Arrow":
                path.pop()
    return False
 
def solve_wumpus_problem():
    grid = create_grid()
    for i in grid:
        print(i)
    path = []
    vis = []
    vis.append((0,0))
    if(dfs(grid,vis,0,0,path)):
        print("Solution found!")
        for i in path:
            print(i)
    else:
        print("No solution!")
 
if _name_ == "_main_":
    solve_wumpus_problem()











------------------------------------------------------------------------------------------------------------------






##Solve Travelling Salesperson Problem using simulated annealing


import random
import math


def create_state(n):
    res = []
    s = set()
    while len(s) < n:
        x = random.randint(0, n - 1)
        s.add(x)
    for i in s:
        res.append(int(i))
    return res


def find_cost(city_map, t):
    l = len(city_map)
    x = random.randint(0, len(city_map) - 1)
    y = random.randint(0, len(city_map) - 1)
    while x == y:
        x = random.randint(0, len(city_map) - 1)
        y = random.randint(0, len(city_map) - 1)
    city_map[x], city_map[y] = city_map[y], city_map[x]
    cost = 0
    for i in range(len(city_map)):
        if t[city_map[i]][city_map[(i + 1) % l]] == 0:
            city_map[x], city_map[y] = city_map[y], city_map[x]
            return -1
        cost = cost + t[city_map[i]][city_map[(i + 1) % l]]
    return cost


def stimulated_annealing(curr_cost, city_map, t):
    for _ in range(100):
        temperature = pow(10, 10)
        cooling_factor = 0.99
        ending_temperature = 0.0001
        while temperature > ending_temperature:
            new_cost = find_cost(city_map, t)
            if new_cost == -1:
                continue
            difference = new_cost - curr_cost
            if difference < 0 or math.exp((-1 * difference) // temperature) > random.randint(0, 1):
                curr_cost = new_cost
            temperature = temperature * cooling_factor
    print("Final path with minimum cost :-")
    print(city_map)
    return curr_cost


if __name__ == "__main__":
    n = int(input("Enter the number of cities : "))
    t = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            print('Enter the distance between city ', i + 1, ' and ', j + 1)
            x = int(input())
            t[i][j] = x
            t[j][i] = x
    city = create_state(n)
    cos = find_cost(city, t)
    result = stimulated_annealing(cos, city, t)
    print("The resulting cost of the final path :-")
    print(result)















------------------------------------------------------------------------------------------------------------------








##zero sum using aplha beta alpha_beta_pruning

import random
import sys

def create_state(num,levels):
    s=set()
    v=[]
    count=1
    while count<num:
        if count*2>num:
            break
        levels=levels+1
        count=count*2

    while len(s)<count:
        a=random.randint(1,count)
        if a not in s:
            s.add(a)
            v.append(a)

    return v

def alpha_beta_pruning(node,depth,alpha,beta,MaximizingPlayer,value,levels):
    if levels==0:
        return value[node]
    if depth==levels+1:  
        return value[node]  
  
    if MaximizingPlayer==True:
        maxEva=-sys.maxint-1        
        for i in range(0,2):
            eva=alpha_beta_pruning((node*2)+i, depth+1, alpha, beta, False, value, levels)  
            maxEva= max(maxEva, eva)   
            alpha= max(alpha, maxEva)      
            if beta<=alpha:  
                break
        return maxEva
    
    else:
        minEva=sys.maxint
        for i in range(0,2):    
            eva= alpha_beta_pruning((node*2)+i, depth+1, alpha, beta, True, value, levels)  
            minEva= min(minEva, eva)   
            beta= min(beta, eva)  
            if beta<=alpha:  
                break
        return minEva

if __name__=="__main__":
    n=int(input("Enter the amount that player A and B have(They have equal amount) : "))
    x=n
    y=n
    print("Money with A : ",x,"    Money with B : ",y)
    while x>0 and y>0:
        levels=0
        state=[]
        t=random.randint(0,1)
        if t==0:
            state=create_state(y,levels)
            final_val=alpha_beta_pruning(0,0,-sys.maxsize-1,sys.maxsize,True,state,levels)
            print("B gives ",final_val," unit money to A")
            x=x+final_val
            y=y-final_val

        else:
            state=create_state(x,levels)
            final_val=alpha_beta_pruning(0,0,-sys.maxsize-1,sys.maxsize,True,state,levels)
            print("A gives ",final_val," unit money to B")
            x=x-final_val
            y=y+final_val

        print("Money with A : ",x,"    Money with B : ",y)

    if y<=0:
        print("A wins the game.")
    elif x<=0:
        print("B wins the game.")









------------------------------------------------------------------------------------------------------------------






##Blocks World Problem and Goal Stack Planning using heuristic function

import copy

visited_states = []

# heuristic fn - number of misplaced blocks as compared to goal state 
def heuristic(curr_state,goal_state):
    goal_=goal_state[3]
    val=0
    for i in range(len(curr_state)):
        check_val=curr_state[i]
        if len(check_val)>0:
            for j in range(len(check_val)):
                if check_val[j]!=goal_[j]:
                    # val-=1
                    val-=j
                else:
                    # val+=1
                    val+=j
    return val
            
# generate next possible solution for the current state
def generate_next(curr_state,prev_heu,goal_state):
    global visited_states
    state = copy.deepcopy(curr_state)
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] = temp1[j] + [elem]
                    if (temp1 not in visited_states):
                        curr_heu=heuristic(temp1,goal_state)
                        # if a better state than previous state of found
                        if curr_heu>prev_heu:
                            child = copy.deepcopy(temp1)
                            return child
    
    # no better soln than current state is possible
    return 0

def solution_(init_state,goal_state):
    global visited_states

    # checking if initial state is already the final state
    if (init_state == goal_state):
        print (goal_state)
        print("solution found!")
        return
    
    current_state = copy.deepcopy(init_state)
    
    # loop while goal is found or no better optimal solution is possible
    while(True):

        # add current state to visited to avoid repetition
        visited_states.append(copy.deepcopy(current_state))

        print(current_state)
        prev_heu=heuristic(current_state,goal_state)

        # generate possible better child from current state
        child = generate_next(current_state,prev_heu,goal_state)
        
        # No more better states are possible
        if child==0:
            print("Final state - ",current_state)
            return
            
        # change current state to child
        current_state = copy.deepcopy(child)  

def solver():
    # maintaining a global visited to save all visited and avoid repetition & infinite loop condition
    global visited_states
    # inputs
    init_state = [[],[],[],['B','C','D','A']]
    goal_state = [[],[],[],['A','B','C','D']]
    # goal_state = [[],[],[],['A','D','C','B']]
    solution_(init_state,goal_state)

solver()




