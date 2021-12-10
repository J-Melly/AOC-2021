#Import List
with open('Day8.txt') as file:
  import_list = file.readlines()

#Perform initial split and strip data
data = []

for i in range(len(import_list)):
  import_list[i] = import_list[i].replace('|', '')
  data.append(list(filter(None, import_list[i].split(' '))))
  
  for j in range(len(data[i])):
    data[i][j] = data [i][j].strip()


#For Loop to decode data line by line
def decode(line):

  #Dictionary to save solved numbers
  output_dict = {0 : '', 1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : '', 7 : '', 8 : '', 9 : ''} 
  
  #Sort strings prior to inputing
  sorted_list = []
  
  for j in range(len(line)):
    sorted_char = sorted(line[j])
    sorted_list.append(sorted_char)

  #First solve for 1,4,7,8
  solved = 0
  while solved < 4:
    for k in range(len(line)):
      if len(line[k]) == 2:
        output_dict[1] = line[k]
        solved += 1
      if len(line[k]) == 4:
        output_dict[4] = line[k]
        solved += 1
      if len(line[k]) == 3:
        output_dict[7] = line[k]
        solved += 1
      if len(line[k]) == 7:
        output_dict[8] = line[k]
        solved += 1
  
  #Solve for 6
  solved = 0
  while solved != 1:
    for k in range(len(line)):
      if len(line[k]) == 6 and line[k].find(output_dict[1]) == -1:
        output_dict[6] = line[k]
        solved += 1

  #Solve for 9
  solved = 0
  while solved != 1:
    for k in range(len(line)):
      if len(line[k]) == 6 and line[k].find(output_dict[4]) > -1:
        output_dict[9] = line[k]
        solved += 1
          
  #Solve for 0
  solved = 0
  while solved != 1:
    for k in range(len(line)):
      if len(line[k]) == 6 and line[k].find(output_dict[1]) > -1 and line[k] != output_dict[9]:
        output_dict[0] = line[k]
        solved += 1
          
  #Solve for 3
  solved = 0
  while solved != 1:
    for k in range(len(line)):
      if len(line[k]) == 5 and line[k].find(output_dict[1]) > -1:
        output_dict[3] = line[k]
        solved += 1

  #Identify common letters between 1 and 6
  common = ''.join(set(output_dict[1]).intersection(output_dict[6]))
  print(common)

  #Solve for 5
  solved = 0
  while solved != 1:
    for k in range(len(line)):
      if len(line[k]) == 5 and line[k] != output_dict[3] and line[k].find(common) > -1:
        output_dict[5] = line[k]
        solved += 1
  
  #Solve for 2
  solved = 0
  while solved != 1:
    for k in range(len(line)):
      if len(line[k]) == 5 and line[k] != output_dict[3] and line[k] != output_dict[5]:
        output_dict[2] = line[k]
        solved += 1

  print(output_dict)

for i in range(len(data)):
  decode(data[i])
