print("title of program: science MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is 12 + 4?")
  print("   a) 10")
  print("   b) 28")
  print("   c) 16")
  print("   d) 6")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is not subtraction.try again."
    score -=1
  elif answer == "b":
    output = "Wrong. This is not multiplication.try again."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!keep going. "
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. This is not division.try again."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "The chemical formula H2 represents")
  print("   a) one hydrogen molecule")
  print("   b) two hydrogen atoms")
  print("   c) one hydrogen atom")
  print("   d) two hydrogen molecules")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!keep going"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. If so, then it will be written as H and H - two hydrogen atoms."
    score -=1
  elif answer == "c":
    output = "Wrong. Clearly the number 2 in the formulae must mean something?"
    score -=1
    
  elif answer == "d":
    output = "Wrong. What's the difference between a molecule and an atom?"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which represents the electronic configuration of a non-metal?")
  print("   a) 2,1")
  print("   b) 2,8,3")
  print("   c) 2,8,8,2")
  print("   d) 2,7")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "b":
    output = "Wrong.  Think again - how are these electron shells related to the periodic table?"
    score -=1
  elif answer == "c":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!keep going"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz! Well done!if you didnt get what you want try again. )

