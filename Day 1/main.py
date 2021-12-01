#Data Import
f = open('Day1.txt', 'r')
import_list = f.readlines()
depth = [int(item) for item in import_list]

#Question 1
count_of_increases = 0

for index in range(0,len(depth)):
  
  if index > 0:

    if depth[index] > depth[index - 1]:
      count_of_increases += 1

print(count_of_increases)

#Question 2
count_of_increases_2 = 0

def sum_window(count):
  return depth[count] + depth[count+1] + depth[count+2]

for index in range(0,len(depth)):
  if index > 0 and index < len(depth) - 2:  #Verify you aren't at the first line or the last two lines
    
    if sum_window(index) > sum_window(index-1):
      count_of_increases_2 += 1
  

print(count_of_increases_2)
