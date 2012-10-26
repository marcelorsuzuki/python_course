# http://www.codeskulptor.org/#user2-eEqjvK2vqpkvmhW-0.py

# ¼ n s2 / tan(π/n).
 
import math

def area (n, s):
    r = ((1 / 4) * n * s ** 2) / math.tan(math.pi / n)
    return r
    
print area(5, 7)