import random

top_of_range = input("Type a maximum number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)	

    if top_of_range <=0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next timeeee.")
    quit()
 
 
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess the random number: ")
	
    if user_guess.isdigit():
	    
        user_guess = int(user_guess)
    
    else:
        print("Please type a number next time.")
        continue
		
    if user_guess == random_number:
		
        print("WIN WIN WIN WIN WIN! Thanks for playing the game")
        break
    
    elif user_guess > random_number:
            print("Lower")
    else:
            print("Higher")
        
print("Took you", guesses, "guesses")

