## HW SOLUTION
l=[10,1,10,10]
h=[5,50,5,1]


def best_income(low, high):
 n = len(low)

 low = [0] + low
 high = [0] + high

 # Initialize an array of booleans to keep track of whether the
 # optimal choice is to take the high-stress job at week i (if we
 # only work weeks 1..i).
 take_high_job = [False] * (n+1)
 opt = [0] * (n+1)
 opt[1] = max(low[1], high[1])

 # We should take the high-stress job at week 1 iff it pays more.
 take_high_job[1] = (high[1] > low[1])

 for i in range(2, n+1):
  low_total = low[i] + opt[i-1]
  high_total = high[i] + opt[i-2]
  opt[i] = max(low_total, high_total)

  # Record which choice produced the higher total
  take_high_job[i] = high_total > low_total

 # Now, to produce a work schedule, work backwards from the end
 # Start at week n
 w = n
 schedule = []
 print(take_high_job)
 while w > 0:
 # If we should take the high-stress job at week w, schedule it
 # and a week off, and proceed to look at week w-2 next
  if take_high_job[w]:
   schedule = ['off', 'High'] + schedule
   w -= 2
  # Otherwise schedule the low-stress job and look at week w-1 next
  else:
    schedule = ['Low'] + schedule
    w -= 1

 print("max profit is:", opt[n])

 for i in range(len(schedule)):
     if schedule[i] == 'off':
         print("take week {} off".format(i+1))
     else:
         print("take {} stress job on week {}".format(schedule[i],i+1))
 return (opt[n], schedule)

best_income(l,h)



########################################################################################################
########################################################################################################
########################################################################################################
# PRACTICE PROBLEM #
NY = [1,4,1]

SF = [20,1,20]

ny = [1,3,20,30]

sf= [50,20,2,4]
def where(loc1,loc2):
    if loc1==loc2:
        v=0
        return v
    else:
        m=10
        return m

def which_month( nt, st):

    n= len(nt)

    m = 10

    nt = [0] + nt
    st = [0] + st

    opt= [0]*(n+1)
    opt[1] = min(nt[1],st[1])
    current_city=[]
    if opt[1] == nt[1]:
        current_city.append("NY")
    else:
        current_city.append("SF")
  
    for i in range(n+1):  
        Ny_cost = opt[i-1]+nt[i]+where(current_city[i],"NY")
        Sf_cost = opt[i-1]+st[i]+where(current_city[i],"SF")
        opt[i] = min(Ny_cost,Sf_cost)  
        if opt[i] == Ny_cost:
         current_city.append("NY")
        else:
         current_city.append("SF")
        
 

    
    print("Start in {} city".format(current_city[0]))
  
    for i in range(2,len(current_city)-1):
        if current_city[i] == current_city[i+1]:
            print("stay in {} city".format(current_city[i]))
            
        else:
            print("move to {} city".format(current_city[i+1]))         
            
    print("total cost is ${}".format(opt[n]))

which_month(NY,SF)
print("-----------------------------")
which_month(ny,sf)