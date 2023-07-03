#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print(""" _____                                               _    _____                                  _                
|  __ \                                             | |  / ____|                                | |               
| |__) |  __ _  ___  ___ __      __  ___   _ __   __| | | |  __   ___  _ __    ___  _ __   __ _ | |_   ___   _ __ 
|  ___/  / _` |/ __|/ __|\ \ /\ / / / _ \ | '__| / _` | | | |_ | / _ \| '_ \  / _ \| '__| / _` || __| / _ \ | '__|
| |     | (_| |\__ \\__ \ \ V  V / | (_) || |   | (_| | | |__| ||  __/| | | ||  __/| |   | (_| || |_ | (_) || |   
|_|      \__,_||___/|___/  \_/\_/   \___/ |_|    \__,_|  \_____| \___||_| |_| \___||_|    \__,_| \__| \___/ |_|   
                                                                                                                  
                                                                                                                  
""")
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=""
for a in range(1,nr_letters+1):
   password+=random.choice(letters)
for b in range(1,nr_symbols+1):
  password+=random.choice(symbols)
for c in range(1,nr_numbers+1):
  password+=random.choice(numbers)
passwords=[i for i in password]
random.shuffle(passwords)
pas=''.join(passwords)
print(f'Ypur New Password is: {pas}')
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P