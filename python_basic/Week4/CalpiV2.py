# CalpiV2.py
from random import random, seed
from time import perf_counter
DARTS = 10000*10000
hits = 0.0
start = perf_counter()
seed(10)
for i in range(1, DARTS+1):
    x, y = random(), random()
    distSq = x**2 + y**2
    if distSq <= 1.0:
        hits += 1
pi = 4 * (hits/DARTS)
print("The π equals to: {}".format(pi))
print("It takes {:.5f}s to calculate".format(perf_counter()-start))