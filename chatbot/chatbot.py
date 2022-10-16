def chatbot_introduction(bot_name, birth_year):
    print(f"Hello, my name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def chatbot_ask_name():
    print("Please, remind "
          "me your name.")
    your_name = input()
    print(f"What a great name "
          f"you have, {your_name}!")


def chatbot_calculate_age():
    print("Let me guess your name.")
    print("Enter remainders of dividing your age by 3,5 and 7.")

    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {your_age}; that`s a good time to start programming!")


def chatbot_count():
    print("Now I will prove to you that I can count to any number you want.")
    max_number = int(input())
    print_number = 1

    while print_number <= max_number:
        print(f"{print_number}!")
        print_number += 1

    print("Completed, have a nice day!")


def chatbot_quiz():
    print("""Let`s test your programming knowledge.
    What is a correct syntax to output "Hello World" in Python?
    1. print("Hello, World").
    2. p("Hello, World").
    3. echo("Hello, World").
    4. echo "Hello, World".""")
    answer = int(input())
    while answer != 1:
        print("Please, try again.")
        answer = int(input())
    print("Completed, have a nice day!")


chatbot_introduction('Good_bot', '2022')
chatbot_ask_name()
chatbot_calculate_age()
chatbot_count()
chatbot_quiz()
print("Congratulations, have a nice day!")