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