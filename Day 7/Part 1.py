#Import List
with open('Day7.txt') as file:
  import_list = file.readlines()
  import_list[0] = import_list[0].strip()

data = import_list[0].split(',')
crabs = [int(item) for item in data]

#Function to determine fuel spent
def fuel(my_list, pos):
  sum = 0
  for i in range(len(my_list)):
    sum += abs(my_list[i] - pos)

  return sum  

fuel_list = []

for i in range(len(crabs)):
  fuel_list.append(fuel(crabs,i))


print(min(fuel_list))
