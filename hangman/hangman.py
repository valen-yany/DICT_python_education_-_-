import random


def announce():
    print("HANGMAN\nThe game will available soon\n")


def hangman(hidden_word):
    print("HANGMAN")
    print("Guess the word:", end="")
    word = input()
    if word == hidden_word:
        print("You survived!")
    else:
        print("You lost!")


def hangman_random():
    vocabulary = ('python', 'java', 'javascript', 'php')
    hidden_word = vocabulary[random.randint(0, len(vocabulary)-1)]
    print("HANGMAN")
    print("Guess the word:", end="")
    word = input()
    if word == hidden_word:
        print("You survived!")
    else:
        print("You lost!")


def hangman_random_hint():
    vocabulary = ('python', 'java', 'javascript', 'php')
    hidden_word = str(vocabulary[random.randint(0, len(vocabulary)-1)])
    hint = hidden_word[0:3] + "-" * (len(hidden_word)-3)
    print("HANGMAN")
    print(f"Guess the word {hint}:", end="")
    word = input()
    if word == hidden_word:
        print("You survived!")
    else:
        print("You lost!")


def hangman_random_attempts():
    vocabulary = ('python', 'java', 'javascript', 'php')
    hidden_word = (vocabulary[random.randint(0, len(vocabulary) - 1)])
    print("HANGMAN\n")
    word = ['-'] * len(hidden_word)
    for i in range(0, 8):
        print("".join(word))
        print("Input a letter:", end="")
        letter = input()

        if hidden_word.count(letter):
            for j in range(0, len(word)):
                if hidden_word[j] == letter:
                    word[j] = letter
        else:
            print('That letter doesn\'t appear in the word', end="\n")
        print()
    print("""Thanks for playing!
We'll see how well you did in the next stage""")


def hangman_with_lives():
    vocabulary = ('python', 'java', 'javascript', 'php')
    hidden_word = (vocabulary[random.randint(0, len(vocabulary) - 1)])
    print("HANGMAN")
    word = ['-'] * len(hidden_word)
    lives = 8
    tested_letters = set()
    while lives > 0:
        print(f'\n{"".join(word)}')
        if "-" not in word:
            print("""You guessed the word!
You survived!""")
            return None
        print("Input a letter:", end="")
        letter = input()
        if letter in tested_letters:
            print("No improvements")
            lives -= 1
        elif letter not in hidden_word:
            print('That letter doesn\'t appear in the word', end="\n")
            lives -= 1
            tested_letters.add(letter)
        else:
            tested_letters.add(letter)
            for j in range(0, len(word)):
                if hidden_word[j] == letter:
                    word[j] = letter
    print("You lost!")


def hangman_with_lives_improved():
    vocabulary = ('python', 'java', 'javascript', 'php')
    hidden_word = (vocabulary[random.randint(0, len(vocabulary) - 1)])
    print("HANGMAN")
    word = ['-'] * len(hidden_word)
    lives = 8
    tested_letters = set()
    while lives > 0:
        print(f'\n{"".join(word)}')
        if "-" not in word:
            print("""You guessed the word!
You survived!""")
            return None
        print("Input a letter:", end="")
        letter = input()
        if letter in tested_letters:
            print("You've already guessed this letter.")
        elif len(letter) > 1:
            print("You should input a single letter")
        elif ord(letter)<ord("a") or ord(letter) > ord("z"):
            print("Please enter a lowercase English letter")
        elif letter not in hidden_word:
            print('That letter doesn\'t appear in the word', end="\n")
            lives -= 1
            tested_letters.add(letter)
        else:
            tested_letters.add(letter)
            for j in range(0, len(word)):
                if hidden_word[j] == letter:
                    word[j] = letter
    print("You lost!")


def hangman_full():
    print("HANGMAN")
    while True:
        print('Type "play" to play the game, "exit" to quit:', end='')
        menu_option = input()
        while menu_option != "play" and menu_option != "exit":
            print('Type "play" to play the game, "exit" to quit:', end='')
            menu_option = input()
        if menu_option == "exit":
            return None
        else:
            vocabulary = ('python', 'java', 'javascript', 'php')
            hidden_word = (vocabulary[random.randint(0, len(vocabulary) - 1)])
            word = ['-'] * len(hidden_word)
            lives = 8
            tested_letters = set()
            while True:
                print(f'\n{"".join(word)}')
                if "-" not in word:
                    print("""You guessed the word!
You survived!
""")
                    break
                print("Input a letter:", end="")
                letter = input()
                if letter in tested_letters:
                    print("You've already guessed this letter.")
                elif len(letter) > 1:
                    print("You should input a single letter")
                elif ord(letter) < ord("a") or ord(letter) > ord("z"):
                    print("Please enter a lowercase English letter")
                elif letter not in hidden_word:
                    print('That letter doesn\'t appear in the word', end="\n")
                    lives -= 1
                    tested_letters.add(letter)
                else:
                    tested_letters.add(letter)
                    for j in range(0, len(word)):
                        if hidden_word[j] == letter:
                            word[j] = letter
                if lives < 1:
                    print("You lost!\n")
                    break


# announce()
# hangman("python")
# hangman_random()
# hangman_random_hint()
# hangman_random_attempts()
# hangman_with_lives()
# hangman_with_lives_improved()
hangman_full()
