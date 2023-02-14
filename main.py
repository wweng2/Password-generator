import random

# Function purpose: take any list and output a random string of element
# from the list as a string that is than return 
def random_generator(Password_length, new_list):
  password = ""
  for i in range(Password_length):
    password += random.choice(new_list)

  return password


def game():
  choice = 0 # The list of alpahbet and number for the list to use
  Alphabet = ["a", "b", "c", "d", "e, "f"", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  number = ["0","1","2","3","4","5","6","7","8","9"]
  special_characters = ["@",".","$","#","%","&"]# Gave the most common special character to be used

  
  # Choice a mode for the password genertor to make a passowrd
  print("Here is the type of generator you can use")
  print("Version 1: Random")
  print("Version 2: Mutlple words password")
  print("Version3: Personal")

  
  choice = int(input("What version would you like:  "))

  
  if (choice == 1):
     # This one is just one that give a pawssord of random character based on length
    second_choice = int(input("How many password do you want: "))
    password_length = int(input("How long do you want your password: "))
    
    new_list = Alphabet + number + special_characters
    for i in range(second_choice):
      
      print(random_generator(password_length, new_list))
 

      stop = str(input("Would you like to exit"))
      
  
      


  elif (choice == 2):# This one is for when an user want to have a someone read able password , they can use a wod they like as a basis
    word_base = str(input("Please put int the word you would like to make a pasword on"))

    password_length = int(input("How long do you want your password: "))

    second_choice = int(input("How many password do you want: "))
    changed_list = number + special_characters
    real_length = password_length - len(word_base)

    for i in range(second_choice):
      print(word_base + random_generator(real_length, changed_list))
    
    
  elif (choice == 3):# This si completing cutomiable and allwo the user to make a password based on what they like.
    password = ""
    password_length = int(input("How long do you want your alphabet portion: "))


    password = random_generator(password_length, Alphabet)
    password_length = int(input("How long do you want your number portion:  "))


    password += random_generator(password_length, number)

    password_length = int(input("How long do you want your specail character portion: "))


    password += random_generator(password_length, special_characters)

    print("Here is your password: " + password)
  else:
    print("Choose the wrong number, please choose one from 1-4")

game()

  

