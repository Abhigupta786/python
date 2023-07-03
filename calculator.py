
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mult(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
op={
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
}
def calculator():
  print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
)
  should_cal=True
  num1=float(input("Enter first number: "))
  for symbol in op:
    print(symbol)
  while should_cal:
    operation=input("Select any Operation: ")
    num2=float(input("Enter Second Number: "))
    function=op[operation]
    ans=function(num1,num2)
    print(f'{num1} {operation} {num2} ={ans}')
    w=input(f'"y" if Want to continue with{ans} or "n" to exit and "c" to clear: ')
    if  w=="y":
      num1=ans
    elif w=="c":
      calculator()
    else:
      print("Thank You fo using")
      should_cal=False
    break
calculator()