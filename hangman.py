def Hangman_Graphic(x):
  print("____")
  print("|   |")
  if x==0:
    print("|")
    print("|")
    print("|")
    print("|")
  if x==1:
    print("|   o")
    print("|")
    print("|")
    print("|")
  if x==2:
    print("|   o")
    print("|   |")
    print("|   |")
    print("|")
  if x==3:
    print("|   o")
    print("|  _|")
    print("|   |")
    print("|")
  if x==4:
    print("|   o")
    print("|  _|_")
    print("|   |")
    print("|")
  if x==5:
    print("|   o")
    print("|  _|_")
    print("|   |")
    print("|   /")
  if x==6:
    print("|   o")
    print("|  _|_")
    print("|   |")
    print("|   /\\")  
  print("|")
  print("====")
  #if x>6:
   # return False

import random

print('Welcome to Hangman!')

with open('wordbank.txt', 'r') as f:
  for line in f:
    line=f.readlines()
word = random.choice(line)

z=0
# Now ask the user to guess the word
guess=list('_')*(len(word)-1)
while list(word)[:-1] != list(guess):
  print(' '.join(guess))  # This joins the guess with the blank spaces.
  letter=input("Guess a letter").upper()
  i=0

  if any(list(word)[x]==letter for x in range(len(word)))==False:
    z+=1
    Hangman_Graphic(z)
    if z>5:
      print("Game Over")
      break
    print('incorrect')

  while i<len(word):
      if list(word)[i]==letter:
        guess[i]=letter
      i+=1
print('it\'s '+word)
