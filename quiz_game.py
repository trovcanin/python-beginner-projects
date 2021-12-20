print("Welcome to my quiz!")

playing = input("Do you want to play? yes/no ")

if playing.lower() == "yes":
    print("Ok, lets play!") 
    score = 0

else:
    print("Ok, maybe some another time :(")

#Question 1
question = input("1.Which port number is used by HTTP? ")
if question.lower() == str(80):
    print("Correct!")
    score += 1

else:   
    print("Sorry, incorrect!")

#Question 2
question = input("Which port number is used by SMTP? ")
if question.lower() == str(25):
    print("Correct!")
    score += 1

else:
    print("Sorry, incorrect.")


print("You got " + str(score) + " questions correct! Congratz" )




