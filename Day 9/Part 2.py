#Import List
with open('Day9.txt') as file:
  my_list = file.readlines()

for i in range(len(my_list)):
  my_list[i] = my_list[i].strip()



#Crawl function will crawl the list to find other locations in basin
def crawl(my_list, i, j):
  basin = [[i,j]]
  counter = 0
  len_basin = len(basin)
 
  while counter < len_basin:
    #Check left. 
    
    if int(my_list[basin[counter][0]][basin[counter][1]-1]) != 9 and basin[counter][1] != 0:
        new_list = [basin[counter][0],basin[counter][1]-1]
        if basin.count(new_list) == 0:
          basin.append(new_list)

    #Check up
    if int(my_list[basin[counter][0]-1][basin[counter][1]]) != 9 and basin[counter][0] != 0:
        new_list = [basin[counter][0]-1,basin[counter][1]]
        if basin.count(new_list) == 0:
          basin.append(new_list)
    
    #Check right
    try:
      if int(my_list[basin[counter][0]][basin[counter][1]+1]) != 9:
        new_list = [basin[counter][0],basin[counter][1]+1]
        if basin.count(new_list) == 0:
          basin.append(new_list)
    except:
      pass
    
    #Check down
    try:
      if int(my_list[basin[counter][0]+1][basin[counter][1]]) != 9:
        new_list = [basin[counter][0]+1,basin[counter][1]]
        if basin.count(new_list) == 0:
          basin.append(new_list)
    except:
      pass
    
    counter += 1
    len_basin = len(basin)
  return len_basin




#Find Low Points and save to list
low_points = []

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

    if sum_check == 4:
      low_points.append([i,j])

basin_sizes = []

for i in range(len(low_points)):
  basin_sizes.append(int(crawl(my_list, low_points[i][0], low_points[i][1])))

basin_sizes.sort(reverse=True)
print(basin_sizes[0]*basin_sizes[1]*basin_sizes[2])
