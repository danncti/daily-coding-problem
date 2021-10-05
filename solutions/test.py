import math

# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)

counter = 0
times = 10000000
r=99999

for i in range(times):
    x = randint(0, r)
    y = randint(0, r)
    cir = math.sqrt((x*x)+(y*y))

    if cir<= r:
        counter+=1

print(4*(counter/(times)))
print(counter)
