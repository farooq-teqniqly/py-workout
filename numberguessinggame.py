from random import randint

print("Welcome to the Guess a Number Game!")

guess_min = 10
guess_max = 30


def main():
    number = randint(guess_min, guess_max)
    guess_correct = False

    while not guess_correct:
        try:
            guess: int = int(
                input(
                    f"I'm thinking of a number between {guess_min} and {guess_max}. What's your guess? "
                )
            )
        except ValueError:
            print("Guess a number!")
            continue

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct!")
            guess_correct = True


if __name__ == "__main__":
    main()
