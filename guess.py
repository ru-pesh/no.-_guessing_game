import random
# random moduele is import to make a random guess
print('\n\n\n\t\t\tNUMBER GUESSING GAME')
print('\nRULES:\n1.You get five chances to guess.\n2.you will get hint after your first chance.')
print('3.The no. guessed by you and computer should be same inorder to win the game.')
# the above lines are rules given to play
b=random.randint(1,10)
cou=1
while cou<6:
    a = int(input('\nGuess a no. between 1 and 100 : '))
    # The above vaariable a just gives user access to enter a no.
    if a==b:
        print('You guessed it correctly, it\'s:',b,'\nYOU WIN!')
        break
    elif a>b and cou !=5:
        print('\nThe correct no. is less than',a,'\nyou still have',5-cou,'chance left')
    elif a<b and cou !=5:
        print('\nThe correct no. is greater than',a,'\nyou still have',5-cou,'chance left')
    else:
        print('\n\nYou are incorrect and Your chances are over \nThe correct no. is',b,'\nYOU LOSE!')
    cou+=1

