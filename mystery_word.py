import random
import os


def choose_difficulty():
    while True:
        answer = input("Easy, Medium, or Hard? ")
        if answer != "":
            return answer[0].lower()


def get_word():
    hard_word_list = []
    medium_word_list = []
    easy_word_list = []
    difficulty = choose_difficulty()
    with open("/usr/share/dict/words", 'r') as f:
        for line in f:
            if len(line[:-1]) >= 4 and len(line[:-1]) <= 6:
                easy_word_list.append(line[:-1])
            if len(line[:-1]) >= 6 and len(line[:-1]) <= 8:
                medium_word_list.append(line[:-1])
            if len(line[:-1]) >= 8:
                hard_word_list.append(line[:-1])
        if difficulty == "e":
            return random.choice(easy_word_list)
        if difficulty == "h":
            return random.choice(hard_word_list)
        else:
            return random.choice(medium_word_list)


def show_board(word, guessed_letters):
    for letter in word:
        letter = letter.upper()
        if letter in guessed_letters:
            print(letter, "", end="")
        else:
            print("_ ", end="")
    print()


def game(word, wrong_guesses, guessed_letters):
    print("Your word contains {} letters.".format(len(word)))
    while wrong_guesses < 8:
        print("\nYou have {} guesses left".format(8 - wrong_guesses))
        show_board(word, guessed_letters)
        guess = guess_letter(guessed_letters)
        guessed_letters.append(guess)
        if guess not in word.upper():
            print("Nope.")
            wrong_guesses += 1
        if len(guessed_letters) - wrong_guesses == len(set(word.lower())):
            show_board(word, guessed_letters)
            print("You win! The word was", word)
            break
        os.system('clear')
    if wrong_guesses == 8:
        print("That was 8 guesses. You lose")
        print("The word was", word)


def guess_letter(guessed_letters):
    while True:
        print()
        guess = input("Guess a letter: ").upper()
        if "guess" in guess.lower():
            for letter in sorted(guessed_letters):
                print(letter, end='')
        elif is_already_guessed(guess, guessed_letters):
            print("You already guessed that letter.")
        elif valid_test(guess) == "too long":
            print("Only guess one letter.")
        elif valid_test(guess) == "not letter":
            print("Your guess must be a letter.")
        else:
            break
    return guess


def valid_test(guess):
    if len(guess) > 1:
        return "too long"
    if not guess.isalpha():
        return "not letter"
    return True


def is_already_guessed(letter, guessed_letters):
    if letter in guessed_letters:
        return True
    return False


def main():
    while True:
        word = get_word()
        wrong_guesses = 0
        guessed_letters = []
        game(word, wrong_guesses, guessed_letters)
        again = input("Play again? ")
        os.system('clear')
        if again == '' or again[0].lower() != "y":
            break
        main()


if __name__ == '__main__':
    main()
