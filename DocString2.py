#Doc String practice

def add(x,y):
    """Result of addition is:"""
    z=x+y
    return z
#print(add.__doc__)
res=add(10,20)
print(add.__doc__,res)