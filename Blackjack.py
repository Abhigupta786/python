import random
print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
def deal_card():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return card
def calculate_score(cards):
  if sum(cards) ==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
def compare(user_score,comp_score):
  if user_score==0:
    print("You won with Blackjack")
  elif comp_score==0:
    print("You Lose ,Dealer has Blackjack")
  elif user_score>21:
    print("You lose")
  elif comp_score>21:
    print("You won")
  elif comp_score==user_score:
    print("Draw")
  elif user_score>comp_score:
    print("You won")
  else:
    print("You Lose")
user_card=[]
comp_card=[]
game_over=False
for i in range(2):
  user_card.append(deal_card())
  comp_card.append(deal_card())
while not game_over:
  user_score=calculate_score(user_card)
  comp_score=calculate_score(comp_card)
  print(f'Users current card: {user_card} Current_Score:{user_score}')
  print(f"Computer's first_card:{comp_card[0]}")
  if user_score==0 or comp_score==0 or user_score>21:
    game_over=True
  else:
    user_choice=input("Type 'y to get new card otherwise type 'n': ").lower()
    if user_choice=='y':
      user_card.append(deal_card())
    elif user_choice=='n':
      game_over=True
    else:
      print('invalid entry ')
while comp_score!=0 and comp_score<17:
  comp_card.append(deal_card())
  comp_score=calculate_score(comp_card)
compare(user_score,comp_score)
print(f'User Score: {user_score}')
print(f'Dealer Score: {comp_score}')
print("Thank You for playing")
 