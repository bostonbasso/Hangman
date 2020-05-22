# Write your code here
import random
import string

word_list = ('python', 'java', 'kotlin', 'javascript')
word = random.choice(word_list)
revealed_word = '-' * len(word)
bad_guesses = 0
max_guesses = 8
letters = set()

print('H A N G M A N')

while True:
    menu_choice = input('Type "play" to play the game, "exit" to quit: ')

    if menu_choice == 'exit':
        break
    elif menu_choice == 'play':
        while bad_guesses < max_guesses and revealed_word != word:
            print(f'\n{revealed_word}')

            guess = input('Input a letter: ')

            if guess in letters:
                print('You already typed this letter')
                continue
            elif len(guess) != 1:
                print('You should print a single letter')
                continue
            elif guess not in string.ascii_lowercase:
                print('It is not an ASCII lowercase letter')
                continue

            letters.add(guess)

            if guess not in word:
                print('No such letter in the word')
                bad_guesses += 1
            else:
                temp = list(revealed_word)

                for i in range(len(word)):
                    if word[i] in letters:
                        temp[i] = word[i]
                    else:
                        temp[i] = '-'

                revealed_word = "".join(temp)

        if revealed_word != word:
            print('You are hanged!')
        else:
            print(f'You guessed the word {revealed_word}!\nYou survived!')
