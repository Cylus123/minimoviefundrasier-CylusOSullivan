valid = False 
while not valid:
  watched_before = input("Have you seen a movie here before ").lower()

  if watched_before == "yes":
    print("Continue with program")
  elif watched_before == "y":
    print("Continue with program")
  elif watched_before == "no":
    print("Display instructions")
  elif watched_before == "n":
    print("Display instructions")
  else:
    print("Invalid input please enter yes or no")