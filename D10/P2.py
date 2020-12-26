with open("wazowski.txt", 'r')as f:
  wazowski=sorted(int(x.strip())for x in f.readlines())

wazowski=[0]+wazowski+[wazowski[-1]+3]

visited={}
def func(c=0):
  if c in visited: return visited[c]
  if len(wazowski)==c+1: return 1;
  ret=0
  for i in range(1, 4):
    try:
      wazowski[c+i]
      if wazowski[c+i]-wazowski[c]<4: ret+=func(c+i)
    except: pass
  visited[c]=ret
  return ret

print(func())
