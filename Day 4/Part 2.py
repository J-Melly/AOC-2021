#Data Import Numbers
f = open('Day4 Numbers.txt', 'r')
import_str = f.readline()

#Comma variables are used to identify numbers between comma positions
first_comma = 0
second_comma = 0
picks = []

for char in range(len(import_str)):
    if import_str[char] == ',':
        second_comma = char
        picks.append(int(import_str[first_comma:second_comma]))
        first_comma = second_comma + 1

#Data Import Bingo Cards
f = open('Day4 Bingo Cards.txt', 'r')
bingo_cards = []
my_list = []

#Create temp list to read in lines
for line in f.readlines():
    my_list.append(line)

#Strip carriage rturns, then strip extra characters at beginning and end, then create a new line, split by ' '.  Append to bingo_cards
for item in range(len(my_list)):
    my_list[item] = my_list[item].rstrip('\n')
    my_list[item].strip()
    line = filter(None, my_list[item].split(' '))
    bingo_cards.append(list(line))

#Convert to ints and create list for each spot on bingo card.  0 indicates a number hasn't been selected, 1 will indicate a number has been selected
for row in range(len(bingo_cards)):
    for col in range(len(bingo_cards[row])):
        bingo_cards[row][col] = [int(bingo_cards[row][col]), 0]



#Function to add a new winner to a running list of winners
def last_winner(cards, winners):
    j = -6  #J += 6 is at the start of the while loop so when a winner is found, j will still equal the row of the winner
    win = 0
    while j < len(cards) - 6:
      j += 6
      total = 0

      #Check if there's a winning row
      for row in range(j, j + 5):
        for col in range(0, 5):
          total = total + cards[row][col][1]
          if total == 5 and winners.count(j) == 0:
            winners.append(j)
            
        total = 0 #reset total before re-running loop

      #Check if there's a winning column
      total = 0
      for col in range(0, 5):
        for row in range(j, j + 5):
          total += cards[row][col][1]
          if total == 5 and winners.count(j) == 0:
            winners.append(j)
          
        total = 0 #reset total before re-running loop

    return winners #return the appended running list of winners
      
    
 ####Part 2
#Run bingo game
i = 0
current_winners = []

#Run the bingo game
while i <= len(picks) - 1 and len(current_winners) < 100: #Stop when the list of winners = the total number of bingo cards
    for row in range(len(bingo_cards)):
        for col in range(len(bingo_cards[row])):
            if bingo_cards[row][col][0] == picks[i]:
                bingo_cards[row][col][1] = 1
    i += 1
    current_winners = last_winner(bingo_cards, current_winners)

sum_unmarked = 0

last_winner_row = current_winners[len(current_winners)-1]

for row in range(last_winner_row,last_winner_row + 5):
  for col in range(0,5):
    if bingo_cards[row][col][1] == 0:
      sum_unmarked += bingo_cards[row][col][0]

print(sum_unmarked*picks[i-1])
