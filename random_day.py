import random

print("Welcome to my Rock, Paper, Scissors game")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player_score = 0
computer_score = 0


while True:



    random_number = random.randint(0, 2)
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

    while choice != 0 and choice != 1 and choice != 2:
       choice = input("Please choose between 0 and 2")


    if choice != 0 and choice != 1 and choice != 2:
        choice = (input("Please choose between 0 and 2"))
    elif random_number == 0 and choice == 0:
        print(f"""
        You chose: 
        {rock}
        The computer chose:
        {rock}
        It's a draw
        """)
        print(f"Your score is {player_score}")
        print(f"The computer score is {computer_score}")


    elif random_number == 0 and choice == 1:
       print(f"""
            You chose:
            {paper}
            The computer chose:
            {rock}
            You have gained a point
            """)
       player_score += 1
       print(f"Your socre is {player_score}")
       print(f"The computer score is {computer_score}")


    elif random_number == 0 and choice == 2:
        print(f"""
                You chose: 
                {scissors}
                The computer chose:
                {rock}
                You lost a point
                """)
        computer_score += 1
        print(f"Your socre is {player_score}")
        print(f"The computer score is {computer_score}")

    elif random_number == 1 and choice == 0:
        print(f"""
                You chose: 
                {rock}
                The computer chose:
                {paper}
                You have lost a point
                """)
        computer_score += 1

        print(f"Your socre is {player_score}")
        print(f"The computer score is {computer_score}")



    elif random_number == 1 and choice == 1:
        print(f"""
                You chose: 
    
                {paper}
    
                The computer chose:
    
                {paper}
                It's a draw
                """)
        print(f"Your socre is {player_score}")
        print(f"The computer score is {computer_score}")


    elif random_number == 1 and choice == 2:
        print(f"""
                You chose: 
                {scissors}
                The computer chose:
                {paper}
                Congratulations! You won a point
                """)
        player_score += 1
        print(f"Your socre is {player_score}")
        print(f"The computer score is {computer_score}")



    elif random_number == 2 and choice == 0:
        print(f"""
                    You chose: 
                    {rock}
                    The computer chose:
                    {scissors}
                   You've lost a point
                    """)
        computer_score += 1
        print(f"Your socre is {player_score}")
        print(f"The computer score is {computer_score}")


    elif random_number == 2 and choice == 1:
        print(f"""
                    You chose: 
                    {paper}
                    The computer chose:
                    {scissors}
                   You've lost a point
                    """)
        computer_score += 1
        print(f"Your socre is {player_score}")
        print(f"The computer score is {computer_score}")


    elif random_number == 2 and choice == 2:
        print(f"""
                    You chose: 
                    {scissors}    
                    The computer chose:
                    {scissors}
                    It's a draw.
                    """)

        print(f"Your socre is {player_score}")
        print(f"The computer score is {computer_score}")


    play_again = input("Do you want to play again? Type yes or no: ")

    if play_again.lower() == "no":
        print("Goodbye!")
        break








