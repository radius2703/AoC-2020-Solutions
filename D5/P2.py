with open('pog.txt', 'r') as f:
  ahhh=[x.strip()for x in f.readlines()]

seats=set()
for i in ahhh:
  id=int(i.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2)
  seats|={id}

for i in range(2**10):
  if (i+1in seats)&(i-1in seats)&(i not in seats): print(i);break