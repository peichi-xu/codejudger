#請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）。
import math
from math import pow
from math import tan

n = eval(input())
s = eval(input())
Area = (n*s*s)/(4*tan(math.pi/n))#math.pi
print('Area =', round(Area,4))
