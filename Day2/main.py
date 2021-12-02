#Data Import into String List
f = open('Day2.txt', 'r')
course = f.readlines()



####Part 1

#Parse List

direction = []
distance = []

for movement in range(len(course)):
  temp_course = course[movement].split()
  direction.append(temp_course[0])
  distance.append(temp_course[1])

#Convert distance to Int
distance = [int(item) for item in distance]

#Iterate list - Perform action on Variable based on list
horizontal = 0
depth = 0

for index in range(len(direction)):
  if direction[index] == 'forward':
    horizontal += distance[index]
  elif direction[index] == 'up':
    depth -= distance[index]
  else:
    depth += distance[index]

print(horizontal * depth)



####Part 2
direction2 = []
distance2 = []

for movement in range(len(course)):
  temp_course = course[movement].split()
  direction2.append(temp_course[0])
  distance2.append(temp_course[1])

#Convert distance to Int
distance2 = [int(item) for item in distance]

#Iterate list - Perform action on Variable based on list
horizontal2 = 0
depth2 = 0
aim2 = 0

for index2 in range(len(direction2)):
  if direction2[index2] == 'forward':
    horizontal2 += distance2[index2]
    depth2 += distance2[index2]*aim2
  elif direction2[index2] == 'up':
    aim2 -= distance2[index2]
  else:
    aim2 += distance2[index2]

print(horizontal2 * depth2)
