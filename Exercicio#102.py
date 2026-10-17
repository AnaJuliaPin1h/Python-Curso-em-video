def fac(num, show=True):
    mul = 1
    if  show:
        for n in range(1,num+1):
            mul*= n
        return mul    
    
    for n in range(num,0,-1):
        print(f"{n}", end=" × " if n > 1 else " = ")
        mul *= n   
    return mul     
        
print(fac(4))