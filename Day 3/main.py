#Import Data
f = open('Day3.txt', 'r')
import_list = f.readlines()
diagnostic = [item.strip() for item in import_list]

####Part 1
gamma = ''
epsilon = ''
data = ''

#Iterate over characters
for char in range(0, len(diagnostic[0])):
#Iterate over lines  
  zero = 0
  one = 0

  for line in range(len(diagnostic)):
    data = diagnostic[line]
    if int(data[char]) == 0:
      zero += 1
    else:
      one += 1
  if one > zero:
    gamma += '1'
    epsilon += '0'
  else:
    gamma += '0'
    epsilon += '1'
 
print(int(gamma,2)*int(epsilon,2))


####Part 2
def trim_list(item, value, char): #item = list, value = 0 or 1, char = position of search
  new_list = []
  for i in range(0,len(item)):
    binary = item[i]
    if int(binary[char]) == int(value):
      #print(binary)
      new_list.append(binary)
  return new_list

oxygen = diagnostic
co2 = diagnostic

data = ''

#Oxygen Generator Rating
for char in range(0, len(oxygen[0])):
  zero = 0
  one = 0

  for line in range(len(oxygen)):
    data = oxygen[line]
    if int(data[char]) == 0:
      zero += 1
    else:
      one += 1
  if one >= zero and len(oxygen) > 1:
    oxygen = trim_list(oxygen, '1', char)
  elif zero > one and len(oxygen) > 1:
    oxygen = trim_list(oxygen, '0', char)

#CO2 Scrubber Rating
for char in range(0, len(co2[0])):
  zero = 0
  one = 0

  for line in range(len(co2)):
    data = co2[line]
    if int(data[char]) == 0:
      zero += 1
    else:
      one += 1
  if one < zero and len(co2) > 1:
    co2 = trim_list(co2, '1', char)
  elif zero <= one and len(co2) > 1:
    co2 = trim_list(co2, '0', char)


print(int(oxygen[0],2)*int(co2[0],2))
