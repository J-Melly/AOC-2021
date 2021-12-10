#Import List
with open('Day9.txt') as file:
  my_list = file.readlines()

for i in range(len(my_list)):
  my_list[i] = my_list[i].strip()

risk_level = 0

for i in range(len(my_list)):
  for j in range(len(my_list[i])):
    sum_check = 0
    
    #Check left.  If first column, don't check value and add to sum
    if j == 0:
      sum_check += 1
    else:
      if int(my_list[i][j-1]) > int(my_list[i][j]):
        sum_check += 1
    
    #Check up, if first row, don't check value and add to sum
    if i == 0:
      sum_check += 1
    else:
      if int(my_list[i-1][j]) > int(my_list[i][j]):
        sum_check += 1

    
    #Check right, error check for index out of range
    try:
      if int(my_list[i][j+1]) > int(my_list[i][j]):
        sum_check += 1
    except:
      sum_check += 1
    
    #Check down error check for index out of range
    try:
      if int(my_list[i+1][j]) > int(my_list[i][j]):
        sum_check += 1
    except:
      sum_check += 1 

    #Increase Risk Level if low point is found
    if sum_check == 4:
      risk_level += int(my_list[i][j]) + 1

print(risk_level)
