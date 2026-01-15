import random

answer = random.randint(1, 9)

Question = input('make a question: ')

print('Question:    ')

if answer == 1:
    print('Question:        ')
    print('Magic 8 ball:    Yes - definitely.')
elif answer == 2:
    print('Question:        ')
    print('Magic 8 ball:    It is decidedly so.')
elif answer == 3:
    print('Question:        ')
    print('Magic 8 ball:    Without a doubt.')
elif answer == 4:
    print('Question:        ')
    print('Magic 8 ball:    Reply hazy, try again.')
elif answer == 5:
    print('Question:        ')
    print('Magic 8 ball:    Ask again later.')
elif answer == 6:
    print('Question:        ')
    print('Magic 8 ball:    Better not tell you now.')
elif answer == 7:
    print('Question:        ')
    print('Magic 8 ball:    My sources say no.')
elif answer == 8:
    print('Question:        ')
    print('Magic 8 ball:    Outlook not so good.')
else:
    print('Question:        ')
    print('Magic 8 ball:    Very doubtful.')
