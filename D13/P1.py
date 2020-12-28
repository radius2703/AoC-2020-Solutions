
with open("horses.txt", 'r') as f:
  lines = [x.strip() for x in f.readlines()]
  departure = int(lines[0])
  buses = [int(x) for x in lines[1].split(',') if x.isdigit()]


actual_departure = int(departure)  # Don't want 2 variables referring to the same place in memory :O
answer = 0

while not answer:
  for i in buses:
    if actual_departure % i == 0:
      answer = (actual_departure - departure) * i
  actual_departure += 1


print(answer)

