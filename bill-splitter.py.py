# write your code here
import random

party = {}
print("Enter the number of friends joining (including you):")
count_of_friends = int(input())
if count_of_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(0, count_of_friends):
        friend = input()
        party[friend] = 0
    print("Enter the total bill value:")
    total = int(input())
    print("""Do you want to use the "Who is lucky?" feature? Write Yes/No:""")
    answer = input()
    if answer == "Yes":
        lucky_one = random.choice(list(party.keys()))
        print(lucky_one, "is the lucky one!")
        for i in party:
            party[i] = round(total / (count_of_friends - 1), 2)
        party[lucky_one] = 0
        print(party)
    elif answer == "No":
        print("No one is going to be lucky")
        for i in party:
            party[i] = round(total / count_of_friends, 2)
        print(party)