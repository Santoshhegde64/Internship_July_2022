# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = int(input())
mu = float(input())
sigma = float(input())
dist_perc = float(input())
z_value = float(input())

stdError = z_value * sigma / math.sqrt(n)

x_l = mu - stdError
x_u = mu + stdError

print(x_l)
print(x_u)