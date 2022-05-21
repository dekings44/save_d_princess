print('Welcome to life hunting forest')

quest = input(' The princess is dying, Would you like to safe the life of the princess? Y or N\n')

if quest == "Y":
    armor = input('Please choose your armoury. Native or Modern\n').lower()
    if armor == "native":
        print(f'Great choice! {armor} You chose is the right armor\n')
        direction = input('Please chose the direction to follow and stay safe while you hunt for the golden egg. Right or Left\n').lower()
        if direction == 'left':
            print(f'Awesome! {direction} path is the safest path')
            action = input('Please choose an action. Please use your armoury.\n You have got all the weapon you need.\n Defend or Attack\n').lower()
            if action == "attack":
                print(f'Great! Please use your armoury, you have got all the weapon you need\n')
                print('Congratulations!!! You just saved the princess')
            else:
                print(f'Game over. You just drown in the river')
        else:
            print(f'{direction} path has so many evil spirits. You can not survive it.\n Try again')
    else:
        print(f'{armor} is not ideal for this type of life saving hunt.\n Try again')
else:
    print('Thank you')