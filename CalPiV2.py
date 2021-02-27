#CalPiV2.py
from random import random
from time import perf_counter
Darts = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1,Darts+1):
    x,y=random(),random()
    dist = pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits+=1
pi = 4*(hits/Darts)
print('圆周率为：{}'.format(pi))
print('用了时间为：{:.2f}s'.format(perf_counter()-start))
