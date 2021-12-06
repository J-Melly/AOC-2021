with open('Day6.txt') as file:
  import_list = file.readlines()
  import_list[0] = import_list[0].strip()

lanternfish = import_list[0].split(',')
lanternfish = [int(item) for item in lanternfish]

count_fish = [0,0,0,0,0,0,0,0,0]

#Creates a list that stores how many of each fish there are with number of days
for i in range(0,8):
  count_fish[i] = lanternfish.count(i)
print(count_fish[0])

for t in range(0,256):
  day_0_count = count_fish[0]  
  
  for j in range(0,len(count_fish)-1):
    count_fish[j] = count_fish[j+1]
    
  count_fish[6] += day_0_count
  count_fish[8] = day_0_count


print(sum(count_fish))
