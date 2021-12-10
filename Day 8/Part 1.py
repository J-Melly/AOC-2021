from pprint import pprint

#Import List
with open('Day8.txt') as file:
  import_list = file.readlines()

#Perform initial split and strip data
data = []

for i in range(len(import_list)):
  data.append(import_list[i].split('|'))
  data[i][0] = data[i][0].strip()
  data[i][1] = data[i][1].strip()

#Split the output digits
for j in range(len(data)):
  data[j][1] = data[j][1].split( ' ')

#Loop through the data and total up string length that totals 2, 4, 3, or 7
total = 0

for k in range(len(data)):
  for l in range(len(data[0][1])):
    if len(data[k][1][l]) == 2 or len(data[k][1][l]) == 4 or len(data[k][1][l]) == 3 or len(data[k][1][l]) == 7:
      total += 1

print(total)
