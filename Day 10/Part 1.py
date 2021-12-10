#Import List
with open('Day10.txt') as file:
  my_list = file.readlines()

for i in range(len(my_list)):
  my_list[i] = my_list[i].strip()

R = len(my_list)

#Instantiate two sets that represent the left and right characters.  Set up a dictionary that maps the right character to the left
left = {'[','(','{','<'}
right = {']',')','}','>'}
my_dict = {
  ']' : '[',
  ')' : '(',
  '}' : '{',
  '>' : '<'
}

#Errors will be appended to a list
errors = []

for r in range(R):
  c = 0
  err = False
  queue = []
  #Run through each string.  When a left character is found, append to a queue.  When a right character is found, 
  #if the last item in queue is the cooresponding left character, pop the left char from the queue.  Else, append the right char to the errors list
  while c < len(my_list[r]) and err == False:
    if my_list[r][c] in left:
      queue.append(my_list[r][c])
    if my_list[r][c] in right and my_dict[my_list[r][c]] == queue[-1]:
      queue.pop()
    elif my_list[r][c] in right and my_dict[my_list[r][c]] != queue[-1]:
      errors.append(my_list[r][c])
      err = True
    c += 1
      

sum = 0

scores = {
  ')' : 3,
  ']' : 57,
  '}' : 1197,
  '>' : 25137
}

for i in range(len(errors)):
  sum += scores[errors[i]]

print(sum)
