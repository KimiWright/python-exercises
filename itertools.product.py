import itertools
#itertools can create infinite loops so use a for loop
for guess in itertools.product("ABCD","xy"):
  guess=''.join(guess)
  print(guess)
