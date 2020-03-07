def countMultiples(n): 
    res = 0; 
    for i in range(1, n + 1): 
        if (i % 3 == 0 or i % 7 == 0): 
            res += 1; 
   
    return res;