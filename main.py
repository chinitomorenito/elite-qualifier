import random 
min = 1
max = 6
print ("Hello I am your personal assistant, Rose and I am a little sassy sometimes...")
user_name = input("What should I call you?")

print(user_name + " nice meeting you!")
age = input("What is your age?")
if int(age) <= 100 :
  print ("well I mean you are alive lol")
else: 
  print ("stop lying goodbye")

fun = input("Do you want to play a game?")
if fun == "yes":
  print ("great, I think i have some dice")
  ans = input("Want to spin the dice?")
  if ans == "yes":
    a = random.randint(1,6)
    print (a)
  else: "wow you are boring"
else: "wow you are boring"
