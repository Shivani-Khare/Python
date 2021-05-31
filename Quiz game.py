'''Program to guess the answwer by giving 4 attempts and displaying
 the score at the end of the program after giving 4 attempts for each.'''

def guess_game (guess, answer):
    global score
    still_guessing = True
    attempt = 0                                                       #count for number of attempts
    
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print ("Hurrayy!! You gave the correct answer!")
            score = score+1
            still_guessing = False
        else:
            if attempt<de3:
                guess = input("Oh no! You gave the wrong answer!")
                attempt = attempt + 1
        if attempt == 3:
            print("The correct answer is", answer)
score = 0
print ("!!!----Welcome to Python Programming Quiz----!!!")
guess_1 = input("Which is the keyword for declaring a function?")
guess_game (guess_1, "def")
guess_2 = input("What is the data type for 123?")
guess_game (guess_2, "int")
guess_3 = input("Who is the father of python?")
guess_game (guess_3, "Guido Van Rossum")

print ("Your total score is : ", score)
