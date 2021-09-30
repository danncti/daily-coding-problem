import math

# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)

hit = 0
times = 1000000
r=9999

for i in range(times):
    x = randint(0, r)
    y = randint(0, r)
    cir = math.sqrt((x*x)+(y*y))

    if cir<= r:
        hit+=1

pi = round(4*(hit/(times)),3)
print(pi)
