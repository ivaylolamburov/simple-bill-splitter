from random import shuffle

number_of_people = int(input('Enter the number of friends joining (including you):\n'))
friends = {}
lucky_one = []
if number_of_people <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for x in range(number_of_people):
        friend = input()
        friends.update({friend: 0})
        lucky_one.append(friend)
    total_value = int(input('Enter the total bill value:\n'))
    price_to_pay = round(total_value / number_of_people, 2)
    for y in friends:
        friends[y] = price_to_pay
    lucky_person = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_person == 'Yes':
        shuffle(lucky_one)
        lucky_friend = lucky_one[0]
        print(f'{lucky_friend} is the lucky one!')
        price_to_pay = round(total_value / (number_of_people - 1), 2)
        for y in friends:
            friends[y] = price_to_pay
        friends[lucky_friend] = 0
        print(friends)
    else:
        print('No one is going to be lucky')
