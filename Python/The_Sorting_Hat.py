Gryffindor = 0
Ravenclaw = 0
Hufflepugg = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk?')
print('     1) Dawn')
print('     2) Dusk')
R1 = int(input('Select 1 or 2: '))
if R1 == 1:
    Gryffindor =+ 1
    Ravenclaw =+ 1 
elif R1 == 2:
    Hufflepugg =+ 1
    Slytherin =+ 1
else:
    print('Wrong input.')

print("Q2) Whem I'm dead, i want people to remember me as: ")
print('     1) The Good')
print('     2) The Great')
print('     3) The Wise')
print('     4) The Bold')
R2 = int(input('Select 1, 2, 3 or 4: '))
if R2 == 1:
    Hufflepugg =+ 2
elif R2 == 2:
    Slytherin =+ 2
elif R2 == 3:
    Ravenclaw =+ 2
elif R2 == 4:
    Gryffindor =+ 2
else:
    print('Wrong input.')

print("Q3) Which kind of instrument most pleases your ear?: ")
print('     1) The violin')
print('     2) The trumpet')
print('     3) The piano')
print('     4) The drum')
R3 = int(input('Select 1, 2, 3 or 4: '))
if R3 == 1:
    Slytherin =+ 4
elif R3 == 2:
    Hufflepugg =+ 4
elif R3 == 3:
    Ravenclaw =+ 4
elif R3 == 4:
    Gryffindor =+ 4
else:
    print('Wrong input.')

print('You points')
print('Gryffindor: ', Gryffindor)
print('Hufflepugg: ', Hufflepugg)
print('Ravenclaw: ', Ravenclaw)
print('Slytherin: ', Slytherin)

#mejorar esto se que se puede

if Gryffindor > Slytherin and Gryffindor > Hufflepugg:
    if Gryffindor > Ravenclaw:
        print('Your house is Gryffindor')
    else:
        print('Your house is Ravenclaw')
elif Slytherin > Gryffindor and Slytherin > Hufflepugg:
    if Slytherin > Ravenclaw:
        print('Your house is Slytherin')
    else:
        print('Your house is Ravenclaw')
elif Hufflepugg > Slytherin and Hufflepugg > Gryffindor:
    if Hufflepugg > Ravenclaw:
        print('Your house is hufflepugg')
    else:
        print('Your house is Ravenclaw')
elif Ravenclaw > Gryffindor and Ravenclaw > Slytherin:
    if Ravenclaw > Hufflepugg:
        print('Your house is Ravenclaw')
    else:
        print('Your house is hufflepugg')