import random
min=1
max=6
yes='y'

print("Rolling the dice....")
result=[]
for x in range(1,11):
  die=random.randint(min, max)
  result.append(die)
  print("die #%i is %i" %(x, die))
while yes!='n':
  a=input("Which dice would you like to reroll? Do not inclued spaces! Example: 157\n")
  for value in a:
    #print(result[int(value)-1])
    #del result[int(value)-1]
    #result.append(die)
    result[int(value)-1]=random.randint(min, max)
  count=0
  for q in result:
    count+=1
    pos=result.index(q)
    print("die #%i is %i" %(count, q))
  yes=input("Reroll? y or n\n")
print("TENZI!")
