def yes_no(question):

  valid = False 
  while not valid:
    watched_before = input(question).lower()
  
    if watched_before == "yes" or watched_before == "y":
      return watched_before
      
    elif watched_before == "no" or watched_before == "n":
      return watched_before
    
    else:
      print("Invalid input please enter yes or no")

valid = False 
while not valid:
  show_instructions = yes_no("Have you watched this before ?: ")
  if show_instructions == "no":
    print("Instructions")
      