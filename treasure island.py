print('')
print('')
print('')
print('')
print('')
print('')
print('')

print('')
print('')
print('Welcome to Treasure Island')

print("You're at a cross road. Where do you want to go?")

directions = input('Type "left" or "right": ').lower().strip()

if directions != "left" and directions != "right":
    print('Please enter either "left" or "right"')
elif directions == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_or_swim = str(input('Type "wait" to wait for a boat. Type "swim" to swim across.'))
    if wait_or_swim != "wait" and wait_or_swim != "swim":
        print('Please enter either "wait" or "swim"')
    elif wait_or_swim == "wait":
        print('You arrive at the island unharmed. There is a house with 3 doors.')
        color_choice = input(str('  One red, one yellow and one blue. Which colour do you choose? '))
        if color_choice != "red" and color_choice != "yellow" and color_choice != "blue":
            print('Please enter either "red" or "yellow" or "bleu"')
        elif color_choice == "red":
            print("It's a room full of fire. Game Over.")
        elif color_choice == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")