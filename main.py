
import time
import random
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

# Welcome screen
name = input("What is your name?: ")
print(f"Welcome to the Fate Algorithm {name}. ")
is_running = True

# The calculation function
def calculations_menu():
    calculations = ("Temperature conversion. Type(T)\nDistance conversion.Type(D)\nWeight conversion. Type(W)\nBasic calculator. Type(C)\nCompound interest calculator. Type(CI)\nCountdown. Type(CD)")
    print(calculations)

     # Distance converter
    def distance ():
            print("Distance converter")

    # Temperature converter 
    def temperature():
        unit = input("Is this temperature in celcius or fahrenheit (C/F): ").upper()
        temp = float(input("Enter the temperature: "))

        if unit == "C":
            temp = round((9 * temp) / 5 + 32, 1)
            print(f"The temperature in Fahrenheit is: {temp} degrees")
        elif unit == "F":
            temp = round((temp - 32) * 5 / 9, 1)
            print(f"The temperature in celsius is: {temp} degrees")
        else:
            print(f"{unit} is an invalid unit of measurement")
    
    # Weight converter calculator function
    def weight():
        unit= input("Is the weight in Kilograms or Pound(K/L): ").upper()
        weight = float(input("Enter the weight: "))
        
        if unit == "K":
            weight = weight * 2.205
            unit = "Lbs"
        elif unit == "L":
            weight = weight / 2.205
            unit = "Kgs"
        else:
            print(f"{unit} was not valid")
        
        print(f"Your weight in {unit} is: {weight} {unit} ")
    
    # Basic calcultor function
    def basic_calculator():
        print ("Welcome to my basic arithmetic calculator \n")

        running = True
        def calculate():
            num1 = float(input("Enter The First Number: "))
            sign_operator = input("Enter Your Operator: ")
            num2 = float(input("Enter Your second Number: "))
            
            if sign_operator == "*":
                print (num1 * num2)
            elif sign_operator == "+":
                print (num1 + num2)
            elif sign_operator == "-":
                print (num1 - num2)
            elif sign_operator == "/":
                print (num1 / num2)
            else:
                print ("Invalid Operator!")
        
        while running:
            action = float(input("For calcuations enter 1, enter 2 to exit: "))
            print(" \n")
            if action == 1:
                calculate()
            else:
                running = False
        
    # Compound interest calculator function
    def compound_interest():
        print("Welcome to the compound interest calculator")
    
        principle = 0
        rate = 0
        time = 0
        currency = input("Enter the currency symbol of your calculation: ")

        while True:
            principle = float(input("Enter the principle amount: "))
            if principle < 0:
                print("Principle cannot be zero.")
            else:
                break
        
        while True:
            rate = float(input("Enter the Rate amount: "))
            if rate < 0:
                print("Rate cannot be zero.")
            else:
                break
                
        while True:
            time = float(input("Enter the time in years: "))
            if time < 0:
                print("Time cannot be zero.")
            else:
                break
            
        total = principle * pow((1 + rate / 100), time)

        print(f"Balance after {time} year/s : \n{currency} {total:.2f}")
    
    # Count down calculator
    def countdown_counter():
        my_timer = int(input("Enter the time in Seconds: "))

        for x in range(my_timer, 0, -1):
            seconds = x % 60
            minutes = int((x / 60)) % 60
            hours = int((x / 3600))
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)
            
        print("Time's up anon")
        
    # Calling Calculation operation functions by user input choice
    
    choice = input (f"What operations would you like to perform today {name}? Enter letters presented above: ").upper()
    if choice == "T":
        return temperature()
    elif choice == "D":
        return distance()
    elif choice == "W":
        return weight()
    elif choice == "C":
        return basic_calculator()
    elif choice == "CD":
        return countdown_counter()
    elif choice == "CI":
        return compound_interest()
    else:
        print("Invalid entry")
 
 
       
#Games only Function block
def games_menu():
    
    # Quiz game function
    def guess_number_game():

        print("Welcome to the number guessing game.")


        # The actual game function
        def the_game():
            
            number = random.randint(1, 100)
            
            while True:
                try:
                    user_guess = int(input("Enter your guess number: "))
                except ValueError:
                    print ("Please enter a valid number.")
                    
                if user_guess < number:
                    print ("Too low. Try again.")
                elif user_guess > number:
                    print ("Too high. Try again.")
                elif user_guess == number:
                    print (f"That is correct {name}")
                    break
        
            play_again()
    
    

        # Play again function
        def play_again():
            
            while True:
                
                again = input(f"Would you like to play again {name}? (Yes/No): ").lower()
                
                if again == "yes":
                    return the_game()
                elif again == "no":
                    break
                else:
                    ("Invalid Entry!")
                    return play_again()
   
        # The main function to call the game function.
        def main():
            while True:
                print("-----------------------------------------------------------------")
                print(f"The game is simple {name}, I give you a number between 1 to 100.")
                proceed = input(f"You have to guess the correct number. Would you like proceed, {name}? (Yes/No): ").lower()
                
                if proceed == "yes":
                    return the_game()
                elif proceed == "no":
                    break
                else:
                    print(f"Invalid entry {name}!")


        main()
    
    #Rock, Paper, Scissors function
    def rockpaper_game():
        while True:
            choices = ["rock", "paper", "scissors"]
            player = None
            computer = random.choice(choices)

            while player not in choices:
                player = input("rock, paper, or scissors?: ").lower()

            if player == computer:
                print("Computer: ", computer)
                print("Player: ", player)
                print("Its a tie")
            elif player == "rock":
                if computer == "paper":
                    print("Computer: ", computer)
                    print("Player: ", player)
                    print("You Lose")
                elif computer == "scissors":
                    print("Computer: ", computer)
                    print("Player: ", player)
                    print("You Win")
            elif player == "scissors":
                if computer == "paper":
                    print("Computer: ", computer)
                    print("Player: ", player)
                    print("You Win")
                elif computer == "scissors":
                    print("Computer: ", computer)
                    print("Player: ", player)
                    print("You Lose")
            elif player == "paper":
                if computer == "rock":
                    print("Computer: ", computer)
                    print("Player: ", player)
                    print("You Win")
                elif computer == "scissors":
                    print("Computer: ", computer)
                    print("Player: ", player)
                    print("You Lose")
            
            play_again = input("Play Again? (yes/No): ").lower()
            
            if play_again !="yes":
                break
            
        print("Thank you for playing with me")
    
    #Quiz Game function
    def quiz_game():
        def new_game():
        
            guesses = []
            correct_guesses = 0
            question_num = 1
    
            for key in questions:
                print("-----------------------")
                print(key)
                for i in options[question_num-1]:
                    print(i)
                guess = input("Enter (A, B, C, or D): ")
                guess = guess.upper()
                guesses.append(guess)
                
                correct_guesses += check_answer(questions.get(key), guess)
                question_num += 1
                
            display_score(correct_guesses, guesses)

        # the check answer function
        def check_answer(answer, guess):
            
            if answer == guess:
                print("CORRECT!")
                return 1
            else:
                print("WRONG!")
                return 0
    

        # display the score function
        def display_score(correct_guesses, guesses):
            print("-----------------------------")
            print("RESULTS")
            print("-----------------------------")
            
            print("Answers: ", end=" ")
            for i in questions:
                print(questions.get(i), end=" ")
            print()
            print("Guesses: ", end=" ")
            for i in guesses:
                print(i, end=" ")
            print()
            
            score = int((correct_guesses/len(questions))*100)
            print(f"Your Score is {str(score)}%")


        # a function for the play again prompt
        def play_again():
            
            rensponse = input("Do you wamt to play again? (Yes/No) ").lower()
            
            if rensponse == "yes":
                return True
            else:
                return False

        questions = {
            "Who created Python?: ": "A",
            "What year was Python created?: ": "B",
            "Python is tributed to which comedy group?: ": "C",
            "Is the Earth Round?: ": "A"
        }

        options = [["A. Guido Van Rossum", "B. Elon Musk", "C. Bills Gate", "D. Mark Zuckerberg"],
                ["A. 1989", "B. 1991", "C. 1974", "D. 1980"],
                ["A. Lonely Island", "B. NL", "C. Monty Pyton", "D. Mark Zuckerberg"],
                ["A. True", "B. False", "C. Debatable", "D. What is Earth"]]


        new_game()

        while play_again():
            new_game()
    
        print("Play again soon .Good Bye")
    games = ("Quiz Game. (QG)\nRock Paper Scissors Game. (RPS)\nNumber Guessing Game. (GN)")
    print(games)
    
    user_play = input("PIck one of the games above and enter the letter represented: ").upper()
    
    if user_play == "QG":
        return quiz_game()
    elif user_play == "RPS":
        return rockpaper_game()
    elif user_play == "GN":
        return guess_number_game()
    else:
        print("Invalid Game entry. Try again")
        return games_menu()
        


#Scripts only Function block
def scripts_menu():
    def banking_program():
        def show_balance(balance):
            print(f" Your Balance is ksh. {balance:.2f}")

        def deposit():
            amount = float(input("Enter the amount to be deposited: "))
            
            if amount < 0:
                print("That is not a valid amount.")
                return 0
            else:
                return amount

        def withdraw(balance):
            amount = float(input("Enter the amount to be witdrawn: ")) 
            
            if amount > balance:
                print("Insufficient funds")
                return 0
            elif amount < 0:
                print("Amount must be above 0")
                return 0
            else:
                return amount

        def the_bank():
            balance = 0
            is_running = True

            while is_running:
                print("-------------------------------")
                print(f"Welcome to the Bank {name}")
                print("1.Show balance")
                print("2.Deposit")
                print("3.Withdraw")
                print("4.Exit")
            
                choice = input("Enter your choice (1-4): ")
            
                if choice == '1':
                    show_balance(balance)
                elif choice == '2':
                    balance += deposit()
                elif choice == '3':
                    balance -= withdraw(balance)
                elif choice == '4':
                    is_running = False
                else:
                    print("That is not a valid option")
                
                    
            print("Thank You For Banking With Us")
            
        the_bank()
        
        
    # Youtube downloader
    def youtube_downloader():
        def download_video(url, save_path):
            try:
                yt = YouTube(url)
                streams = yt.streams.filter(progressive=True, file_extension="mp4")
                highest_res_stream = streams.get_highest_resolution()
                highest_res_stream.download(output_path=save_path)
                print("Video dowwnloaded successfully!")
            
            
            
            except Exception as e:
                print(e)
       
        url = ""
        save_path = "c:/Users/OWNER/Downloads/YouTube"

        download_video(url, save_path)


        def open_file_dialog():
            folder = filedialog.askdirectory()
            if folder:
                print(f"Selected folder: {folder}")
            return folder

        if __name__ == "__main__":
            root = tk.Tk()
            root.withdraw()
            
            video_url = input("Enter your youtube video download link: ")
            save_dir = open_file_dialog()
            
            if save_dir:
                print("Started download............")
                download_video(video_url, save_dir)
            else:
                print("Invalid save location.")
    
    # Calling the scripts
    my_scripts = "For Banking Program Type (BP)\nFor Youtube download script Type (YD)"
    print(my_scripts)
    
    user_script = input("Enter the letter representing the script you would like to use as shon above: ").upper()
    
    if user_script == "BP":
        return banking_program()
    elif user_script == "YD":
        return youtube_downloader()
    else:
        print("Script does not exist. Try again")
        return scripts_menu()
    

def first_choice():
    user_input = int(input("What would you like today? \nFor calculations press 1\nFor games press 2\nFor scripts press 3: "))
    
    if user_input == 1:
        return calculations_menu()
    elif user_input == 2:
        return games_menu()
    elif user_input == 3:
        return scripts_menu()
    else:
        print("Invalid entry")
    

    
# Main loop to call all functions
while is_running:
    menu_request = input(f"To continue press (Y). press anything to exit the program: ").lower()
    
    if menu_request == "y":
        first_choice()
    else:
        print(f"Thank you for visiting {name}")
        is_running = False
