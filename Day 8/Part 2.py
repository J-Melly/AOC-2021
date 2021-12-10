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

#Function to check if characters are in a string
def char_find(str1, chars):
  sum = 0

  for i in range(len(chars)):
    if str1.find(chars[i]) > -1:
      sum += 1
      
  if sum == len(chars):
    return True
  else:
    return False


#For Loop to decode data line by line
def decode(line):

  #Dictionary to save solved numbers
  output_dict = {0 : '', 1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : '', 7 : '', 8 : '', 9 : ''} 
  
  #Sort strings prior to inputing
  sorted_list = []

  for j in range(len(line)):
    sorted_chars = sorted(line[j])
    temp = ''.join(sorted_chars)
    sorted_list.append(temp)

  #First solve for 1,4,7,8
  solved = 0
  while solved < 4:
    for k in range(len(sorted_list)):
      if len(sorted_list[k]) == 2:
        output_dict[1] = sorted_list[k]
        solved += 1
      if len(sorted_list[k]) == 4:
        output_dict[4] = sorted_list[k]
        solved += 1
      if len(sorted_list[k]) == 3:
        output_dict[7] = sorted_list[k]
        solved += 1
      if len(sorted_list[k]) == 7:
        output_dict[8] = sorted_list[k]
        solved += 1

  #Solve for 6
  solved = 0
  while solved < 1:
    for k in range(len(sorted_list)):
      if len(sorted_list[k]) == 6 and char_find(sorted_list[k],output_dict[1]) == False:
        output_dict[6] = sorted_list[k]
        solved += 1
  
  #Solve for 9
  solved = 0
  while solved < 1:
    for k in range(len(sorted_list)):
      if len(sorted_list[k]) == 6 and char_find(sorted_list[k],output_dict[4]) == True:
        output_dict[9] = sorted_list[k]
        solved += 1

  #Solve for 0
  solved = 0
  while solved < 1:
    for k in range(len(sorted_list)):
      if len(sorted_list[k]) == 6 and char_find(sorted_list[k],output_dict[1]) == True and sorted_list[k] != output_dict[9]:
        output_dict[0] = sorted_list[k]
        solved += 1
  
  #Solve for 3
  solved = 0
  while solved < 1:
    for k in range(len(sorted_list)):
      if len(sorted_list[k]) == 5 and char_find(sorted_list[k],output_dict[1]) == True:
        output_dict[3] = sorted_list[k]
        solved += 1
    
  #Identify common_char letters between 1 and 6
  common_char = ''.join(set(output_dict[1]).intersection(output_dict[6]))

  #Solve for 5
  solved = 0
  while solved < 1:
    for k in range(len(sorted_list)):
      if len(sorted_list[k]) == 5 and sorted_list[k] != output_dict[3] and char_find(sorted_list[k],common_char) == True:
        output_dict[5] = sorted_list[k]
        solved += 1
  
  #Solve for 2
  solved = 0
  while solved < 1:
    for k in range(len(sorted_list)):
      if len(sorted_list[k]) == 5 and sorted_list[k] != output_dict[3] and sorted_list[k] != output_dict[5]:
        output_dict[2] = sorted_list[k]
        solved += 1
    

  #Invert Dictionary:
  inv_dict = {v:k for k, v in output_dict.items()}
  solved_number = ''
  solved_number = str(inv_dict[sorted_list[10]]) + str(inv_dict[sorted_list[11]]) + str(inv_dict[sorted_list[12]]) + str(inv_dict[sorted_list[13]])
  return int(solved_number)

sum = 0

for i in range(len(data)):
  sum += decode(data[i])
print(sum)
