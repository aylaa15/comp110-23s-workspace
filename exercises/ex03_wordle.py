"""EX03 - Wordle."""
__author__ = "730386998"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, single_char: str) -> bool:
    """Searching different parameters and lengths in strings"""
    assert len(single_char) == 1 
    counter: int = 0
    while counter < len(word):
        if word[counter] == single_char:
            return True
        counter = counter + 1
    return False  

def emojified(guess: str, secret:str) -> str:
    """Comparing two strings of the same length and getting emojis that codify the two strings"""
    assert len(secret) == len(guess)
    i: int = 0
    output: str = ""
    while i < len(secret):
        if secret[i] == guess[i]:
            output = output + GREEN_BOX 
        else:
            if contains_char(secret, guess[i]):
                output = output + YELLOW_BOX
            else:
                output = output + WHITE_BOX 
        i = i + 1
    return output 


def input_guess(length_guess: int) -> str:
    """Prompting for a user to guess until guessing the correct expected length"""
    guess: str = str(input(f"Enter a {length_guess} character word: "))
    while len(guess) != length_guess:
        guess = str(input(f"That wasn't {length_guess} chars! Try again: "))
    return guess 

def main() -> None:
    """The entrypoint of the program and main game loop."""
    num_turns: int = 1
    max_turns: int = 6
    secret: str = "codes"
    checker: bool = True
    while num_turns <= max_turns and checker:
        print (f"=== Turn {num_turns}/{max_turns} ===")
        guess = input_guess(5)
        print(emojified(guess, secret))

        if guess == secret: 
            checker = False 
            print(f"You won in {num_turns}/{max_turns} turns!")
        num_turns = num_turns + 1 

    if guess != secret:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()