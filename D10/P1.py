with open("wazowski.txt", 'r')as f:
  wazowski=sorted(int(x.strip())for x in f.readlines())

one=twee=1

for i in range(1,len(wazowski)):
  delta=wazowski[i]-wazowski[i-1]
  if delta==1:one+=1
  if delta==3:twee+=1

print(one*twee)
