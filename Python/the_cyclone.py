height = int(input('Your height(cm): '))
Credits = int(input('Your credits: '))

if height >= 137 and Credits >=10:
    print('Enjoy the ride!')
elif height <137 and Credits >=10:
    print('You are not tall enough to ride.')
elif height >= 137 and Credits <10:
    print("You don't have enough credits.")
else:
    print('You dont have met either requirement.')