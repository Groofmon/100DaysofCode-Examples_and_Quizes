import random

word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = ["_" for i in chosen_word]
# blanked_guess = "".join(blanked_guess)
guessed_letters = []
hangman_stages = [
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    '''
]


health = 6
while True:
    print("".join(display))

    # Control if Win or Lose
    if not ("_" in display):
        print("You Win!")
        break
    elif health == 0 and "_" in display:
        print("Game Over, Hangman died!")
        break

    guess = input("Guess letter of the word: ").lower().strip()
    if guess in guessed_letters:
        print("!!! You already guessed this letter, choose another letter !!!")
        continue
    else:
        guessed_letters.append(guess)

    if guess in chosen_word:
        index = 0
        for i in chosen_word:
            if i == guess:
                display[index] = chosen_word[index]
            index += 1

        #print("".join(blanked_guess))
    else:
        health -=1
        print(hangman_stages[6 - health])

        print(f"Wrong guess! health: {health+1} -> {health}")

