import random
import os

def random_word():
    file_name = 'fruits.txt'
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)

    with open(file_path) as f:
        fruits = [row for row in f.readlines()]
        return random.choice(fruits)

word = random_word()

def game(word):
    lines = "_"
    for _ in range(len(word) - 2):
        lines = lines + "_"

    print("Guess the word. 5 mistakes left.")

    i = 5
    while i > 0:
        print(lines)
        if lines.find("_") == -1:
            print("You won the game.")
            break

        x = input("Guess a letter: ").lower()

        for j in range(len(word) - 1):
            if x == word[j]:
                lines = lines[0:j] + x + lines[j + 1:]
        if word.find(x) == -1:
            i -= 1

        print(f"Guess the word. {i} mistakes left")

    if i == 0:
        print(f'''Ooops! You lost the game.
    Answer: {word}''')

game(word)
