import random

def heron_sqrt(x):
     
    g = random.randint()
    if enough(x - g * g):
        return g
    else:
        g = (g + x / g) / 2  
        heron_sqrt(g)

    
