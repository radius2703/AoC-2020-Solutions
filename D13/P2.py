
with open("horses.txt", 'r') as f:
  lines = [x.strip() for x in f.readlines()]
  buses = [x for x in lines[1].split(',')]


# The next 19 lines are taken from: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python

def chinese_remainder_theorem(n, a):
  prod = __import__('functools').reduce(lambda a,b: a*b,n)
  total = sum([a_i*mul_inv(prod//n_i, n_i)*(prod//n_i) for n_i,a_i in zip(n, a)])
  return total%prod


def mul_inv(a, b):
  x0,x1,b0 = 0,1,b
  if b==1:
    return 1
  while a>1:
    q = a//b
    a,b = b,a%b
    x0,x1 = x1-q*x0,x0
  if x1<0:
    x1 += b0
  return x1


indices = [-x for x, bus in enumerate(buses) if bus.isdigit()]
ans = chinese_remainder_theorem(
  [int(x) for x in buses if x.isdigit()], indices)

print(ans)

