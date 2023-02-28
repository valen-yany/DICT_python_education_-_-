import random


def set_test():
    difficulties = {'1': 'simple operations with numbers 2-9', '2': 'integral squares of 11-29',
                    '3': 'integer square roots of 1 - 2500'}
    yes = ('Yes', 'y', 'YES', 'yes')
    while True:
        print('Which level do you want? Enter a number:')
        for key, value in difficulties.items():
            print(f'{key} - {value}')
        difficulty = input().strip(' ')
        while difficulty not in difficulties.keys():
            for key, value in difficulties.items():
                print(f'{key} - {value}')
            difficulty = input().strip(' ')
        mark = questions(difficulty)
        save = input(f'Your mark is {mark}/5. Would you like to save the result? Enter yes or no.\n')
        if save in yes:
            name = input('What is your name?\n')
            f = open('result.txt', 'a')
            f.write('%s: %d/5 in level %s (%s)\n' % (name, mark, difficulty, difficulties[difficulty]))
            f.close()
            print('The results are saved in "results.txt".')
        if input('Do you want to write a new test? Enter yes or no\n') not in yes:
            print('Goodbye!')
            break


def questions(difficult):
    mark = 5
    if difficult == '1':
        for i in range(5):
            number1, number2, operator = random.randint(2, 9), random.randint(2, 9), random.choice(['+', '-', '*'])
            if number2 > number1: number1, number2 = number2, number1
            question = '%d %s %d\n' % (number1, operator, number2)
            answer = input(question)
            while not answer.isdigit():
                answer = input(f'Incorrect format. Try again!\n{question}')
            if operator == '+' and number1 + number2 == int(answer):
                print("Right!")
            elif operator == '-' and number1 - number2 == int(answer):
                print("Right!")
            elif operator == '*' and number1 * number2 == int(answer):
                print("Right!")
            else:
                print('Wrong!')
                mark -= 1
    elif difficult == '2':
        for i in range(5):
            number = random.randint(11, 29)
            answer = input(f'{number}\n')
            while not answer.isdigit():
                answer = input(f'Incorrect format. Try again!\n{number}\n')
            if int(answer) == number ** 2:
                print('Right!')
            else:
                print('Wrong!')
                mark -= 1
    elif difficult == '3':
        for i in range(5):
            number = random.choice([x**2 for x in range(1, 50)])
            answer = input(f'{number}\n')
            while not answer.isdigit():
                answer = input(f'Incorrect format. Try again!\n{number}\n')
            if int(answer) == number ** 0.5:
                print('Right!')
            else:
                print('Wrong!')
                mark -= 1
    return mark


set_test()
