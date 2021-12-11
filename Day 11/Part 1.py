from pprint import pprint

flash_count = 0

#Function to increase surrounding octopus numbers by 1 if an octopus flashes
def flashes(my_list, x, y):
  for k in range(8):
    global flash_count
    
    try:
      if x+dir_x[k] >= 0 and y+dir_y[k] >= 0: #Verify the new coordinates are a positive number.  A negative number won't throw an error
        if my_list[x+dir_x[k]][y+dir_y[k]] != 0: #If an octopus is already equal to zero, then it just flashed and won't increase the power again
          my_list[x+dir_x[k]][y+dir_y[k]] += 1
          if my_list[x+dir_x[k]][y+dir_y[k]] > 9: #If an octopus flashes, call the flashes function and send the new coordinates
            flash_count += 1
            my_list[x+dir_x[k]][y+dir_y[k]] = 0
            my_list = flashes(my_list, x + dir_x[k], y + dir_y[k])
    except:
      pass

  return my_list

#Import List
with open('Day11.txt') as file:
  import_list = file.readlines()

for i in range(len(import_list)):
  import_list[i] = import_list[i].strip()

R = len(import_list)
C = len(import_list[0])

my_list = [[0 for i in range(C)] for i in range(R)]

for i in range(R):
  for j in range(C):
    string = import_list[i]
    my_list[i][j] = int(string[j])


dir_x = [0, 1, 1, 1, 0, -1 , -1, -1] #X coordinate directions when a octopus flashes, starting at 12 o'clock
dir_y = [-1, -1, 0, 1, 1, 1, 0, -1] #Y coordinate directions when a octopus flashes, starting at 12 o'clock, negative indicates up
R = len(my_list)
C = len(my_list[0])

#First loop adds one to every power level
for steps in range(100):
  for i in range(R):
    for j in range(C):
      my_list[i][j] += 1

#Second loop checks if there was a flash and calls function
  for i in range(R):
    for j in range(C):
      if my_list[i][j] > 9:
        flash_count += 1
        my_list[i][j] = 0
        my_list = flashes(my_list, i, j)


print(flash_count)
