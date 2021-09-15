def printknapSack(W, wt, val, n): 
    K = [[0 for w in range(W + 1)] for i in range(n + 1)] 
              
    # Build table K[][] in bottom 
    # up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
             K[i][w] = 0
  
    # If weight of the nth item is 
    # more than Knapsack of capacity W, 
    # then this item cannot be included 
    # in the optimal solution 
            if (wt[i-1] <= w):          
              K[i][w] = max(val[n-1] + printknapSack(W-wt[n-1], wt, val, n-1),printknapSack(W, wt, val, n-1))
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
            else: 
                 K[i][w] =  printknapSack(W, wt, val, n-1) 
    #K = sortRowWise(K)
    # stores the result of Knapsack 
    res = K[n][W] 
    print(res) 
      
    w = W 
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        # either the result comes from the 
        # top (K[i-1][w]) or from (val[i-1] 
        # + K[i-1] [w-wt[i-1]]) as in Knapsack 
        # table. If it comes from the latter 
        # one/ it means the item is included. 
        if res == K[i - 1][w]: 
            continue
        else: 
  
            # This item is included. 
            print(wt[i - 1]) 
              
            # Since this weight is included 
            # its value is deducted 
            res = res - val[i - 1] 
            w = w - wt[i - 1] 

# Driver code 
val = [7,9,5,12,14,6,12] 
wt = [ 3, 4, 2, 6,7,3,5 ] 
W = 15
n = len(val) 
      
printknapSack(W, wt, val, n) 