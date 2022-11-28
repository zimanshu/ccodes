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