#Import List
with open('Day10.txt') as file:
  my_list = file.readlines()

for i in range(len(my_list)):
  my_list[i] = my_list[i].strip()

R = len(my_list)

#Instantiate two sets that represent the left and right characters.  Set up a dictionary that maps the right character to the left and left to right
left = {'[','(','{','<'}
right = {']',')','}','>'}
my_dict = {
  ']' : '[',
  ')' : '(',
  '}' : '{',
  '>' : '<',
  '[' : ']',
  '(' : ')',
  '{' : '}',
  '<' : '>'
}

scores = {
  '(' : 1,
  '[' : 2,
  '{' : 3,
  '<' : 4
}
sums = []


for r in range(R):
  c = 0
  err = False
  line_sum = 0
  queue = []

  #Deteremine if the line has a error using the same logic as part 1
  while c < len(my_list[r]) and err == False:
    if my_list[r][c] in left:
      queue.append(my_list[r][c])
    if my_list[r][c] in right and my_dict[my_list[r][c]] == queue[-1]:
      queue.pop()
    elif my_list[r][c] in right and my_dict[my_list[r][c]] != queue[-1]:
      err = True
    c += 1
  
  #if no error was found, add scores to the line_sum by popping off the end of the queue and looking up the score in the scores dictionary
  while len(queue) > 0 and err == False:
    line_sum = line_sum * 5 + scores[queue.pop()]
  #If no error was found in the row, append the line_sum to the sums list
  if err == False:
    sums.append(line_sum)

#Sort and calculate the middle number of the list
sums.sort()
print(sums[int(len(sums)/2-.5)])
