"""EX02 - One shot wordle."""
__author__ = "730386998"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

SECRET: str = "python"
guess: str = str(input("What is your 6-letter guess? "))
playing: bool = True 

while playing:
    if guess == SECRET:
        print("Woo! You got it!")
        playing = False 
    else:
        while len(guess) != 6:
            guess = str(input("That was not 6 letter! Try again: "))
        if guess != SECRET:
            print("Not quite. Play again soon! ")
            playing = False

i: int = 0
output: str = ""
while i < len(SECRET):
    if guess[i] == SECRET[i]:
        output = output + GREEN_BOX
    else:
        exists: bool = False
        indices: int = 0
        while (exists != True) and (indices < len(SECRET)):
            if SECRET[indices] == guess[i]:
                exists = True
            else:
                indices = indices + 1
        if exists == True:
            output = output + YELLOW_BOX
        else:
            output = output + WHITE_BOX
    i = i + 1
print(output)
