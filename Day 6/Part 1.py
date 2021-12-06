with open('Day6.txt') as file:
  import_list = file.readlines()
  import_list[0] = import_list[0].strip()

lanternfish = import_list[0].split(',')
lanternfish = [int(item) for item in lanternfish]

for t in range(0,80):
  for i in range(len(lanternfish)):  
    if lanternfish[i] == 0:
      lanternfish[i] = 6
      lanternfish.append(8)
    else:
      lanternfish[i] -= 1


print(len(lanternfish))
