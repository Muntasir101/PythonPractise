player_1 = input('Rock,Paper or Scissors').strip(' ').lower()
player_2 = input('Rock,Paper or Scissors').strip(' ').lower()
if player_1 == player_2:
  print('It`s tie')
elif (player_1 == 'rock' and player_2 == 'scissors') or \
        (player_1 == 'paper' and player_2 == 'rock') or \
        (player_1 == 'scissors' and player_2 == 'paper'):
  print('player1 is winner')
elif (player_2 == 'rock' and player_1 == 'scissors') or \
        (player_2 == 'paper' and player_1 == 'rock') or \
        (player_2 == 'scissors' and player_1 == 'paper'):
  print('player2 is winner')
else:
 print('Error happen')

