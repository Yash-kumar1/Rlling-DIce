import random
def Start_Game(start,end):
    return random.randrange(start, end)
    
name=input('Enter Your Name: ').split()

print(f'\nHey! {name}. Welcome to the Roll Dice Game')
print('\nEnter your Die Range. Example: 1 6. Then Rolling Gave the Number between the 1 and 6')
print()
start,end=map(int,input('Enter your Range (Remember Given a space between them) : ').split(' '))
print(Start_Game(start,end))





