def retrocontador0(e):
    print("{},".format(e), end="")
    
    if e > 0:
        retrocontador0(e-1)
    
retrocontador0(10)