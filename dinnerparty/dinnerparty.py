import random


def who_is_lucky(friend_list: dict):
    Name = random.choice(list(friend_list.keys()))
    print(f"{Name} is the lucky one!\n")
    return Name


def dinnerparty_friendlist():
    friend_list = dict()
    print("Enter the number of friends joining (including you):")
    number_of_members = int(input())
    if number_of_members <= 0:
        print("\nNo one is joining for the party")
        exit()
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        for i in range(0, number_of_members):
            friend: str = input()
            friend_list[friend] = 0
        return friend_list


def dinnerparty_bill_division(friend_list: dict):
    print("\nEnter the total amount:")
    amount = int(input())
    print("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    answer = input()
    if answer == 'Yes':
        lucky_one = who_is_lucky(friend_list)
        if amount % (len(friend_list) - 1) == 0:
            pay = int(amount / (len(friend_list) - 1))
        else:
            pay = round(amount / (len(friend_list) - 1), 2)
        for friend in friend_list:
            if friend == lucky_one:
                friend_list[friend] = 0
                continue
            friend_list[friend] = pay
    else:
        print("\nNo one is going to be lucky.")
        if amount % len(friend_list) == 0:
            pay = int(amount / len(friend_list))
        else:
            pay = round(amount / len(friend_list), 2)
        for friend in friend_list:
            friend_list[friend] = pay
    print(friend_list)

friend_list = dinnerparty_friendlist()
dinnerparty_bill_division(friend_list)
