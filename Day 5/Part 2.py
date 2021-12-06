#Data Import Numbers
f = open('Day5.txt', 'r')
import_list = f.readlines()

#Replace format list and convert to a 4 by x 2D array.  Col 0->3 will equal x1, y1, x2, y2
for line in range(len(import_list)):
  import_list[line] = import_list[line].replace(' -> ', ',')
  import_list[line] = import_list[line].strip()
  
  import_list[line] = filter(None, import_list[line].split(','))
  import_list[line] = list(import_list[line])


#Initialize and add data to coordinate list
x_max = 0
y_max = 0

coord_list = [[0]*len(import_list[0]) for x in range(len(import_list))]
for i in range(len(import_list)):
  for j in range(len(import_list[0])):
    coord_list[i][j] = int(import_list[i][j]) 
    
    #Determine the max x and y locations while building coord_list
    if (j == 0 or j == 2) and coord_list[i][j] > x_max - 1:
      x_max = coord_list[i][j] + 1

    if (j == 1 or j == 3) and coord_list[i][j] > y_max - 1:
      y_max = coord_list[i][j] + 1


#Create a 'map' based on coordinates
map_list = [[0]*y_max for x in range(0,x_max)]


#Loop coordinates and build out map
for line in range(len(coord_list)):
  #Vertical Line
  if coord_list[line][0] == coord_list[line][2]:
    x = coord_list[line][0]
    y1 = min(coord_list[line][1],coord_list[line][3])
    y2 = max(coord_list[line][1],coord_list[line][3])

    for item in range(y1, y2+1): #Iterate over coordinates and ensure the range is set smallest to largest
      map_list[item][x] += 1

  #Horizontal Line
  elif coord_list[line][1] == coord_list[line][3]:
    y = coord_list[line][1]
    x1 = min(coord_list[line][0],coord_list[line][2])
    x2 = max(coord_list[line][0],coord_list[line][2])

    for item in range(x1, x2+1): #Iterate over coordinates and ensure the range is set smallest to largest
      map_list[y][item] += 1
 
  #Diagonal lines
  else:
    
    #Set x1y1 to the left most coordinates and the x2y2 to the right most
    if coord_list[line][2] > coord_list[line][0]:
      y1 = coord_list[line][1]
      y2 = coord_list[line][3]
      x1 = coord_list[line][0]
      x2 = coord_list[line][2]
    else:
      y2 = coord_list[line][1]
      y1 = coord_list[line][3]
      x2 = coord_list[line][0]
      x1 = coord_list[line][2]

    #set an x and y position and then iterate along the line until reaching x2y2
    x_pos = int(x1)
    y_pos = int(y1)

    while x_pos != x2 + 1:
      map_list[y_pos][x_pos] += 1
      x_pos += 1
      if y2 < y1:
        y_pos -= 1
      else:
        y_pos += 1


    #Calculate overlaps > 1
count = 0 
for i in range(len(map_list)):
  for j in range(len(map_list[0])):
    if map_list[i][j] > 1:
      count += 1

print(count)
