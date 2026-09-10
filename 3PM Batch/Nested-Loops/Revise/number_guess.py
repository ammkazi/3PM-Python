# Number guessing game

import random

max_attempt = 7

print("=" * 44)
print(f"{'VISUAL LABS NUMBER GUESSING GAME':^44}")
print("=" * 44)

playing = True
rounds_won = 0
rounds_played = 0

while playing:
    secret = random.randint(1,100)
    attempts = 0
    won = False-
    rounds_played +=1

    print(f"\nI am thinking of a number between {1} and {100}.")
    print(f"You have total {max_attempt} attempts.")

    while attempts < max_attempt:
        raw = input(f"Attempt {attempts+1}: ")

        if not raw.isdigit():
            print(f"Please enter a whole number. That did not count!")
            continue

        guess = int(raw)
        if guess < 1 or guess > 100:
            print("Stay between 1 and 100. That did not count!")
            continue
        attempts += 1

        if guess < secret:
            print("Too Low")
        elif guess > secret:
            print("Too high")
        else:
            won = True
            break

    if won:
        score = int(100 * ((max_attempt - attempts+1) / max_attempt))
        rounds_won += 1
        print(f"\nCorrect!! You found {secret} number in {attempts} attempts!")
        print(f"Your score is: {score}/100")
    else:
        print(f"\nOut of attempts. The number was {secret}.")
        print("Score: 0/100")

    again = input("\n Do you want to play again: (y/n): ").lower()
    playing = again == "y"

print(f"\nYou won {rounds_won} of {rounds_played} rounds. Thanks for playing!")
