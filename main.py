import sys
import os
from datetime import datetime

def display_home_screen():
    """Displays the home screen menu and handles user input."""
    while True:
        print("=" * 40)
        print(" Welcome to Fitness Tracker CLI! ")
        print("=" * 40)
        print("\nTrack your fitness journey with these features:")
        print("- Log your workouts and track your progress.")
        print("- View and filter your workout history.")
        print("- Set and manage fitness goals.")
        print("- Access helpful tips and commands.")
        print("- Get motivational fitness tips to stay on track.")
        
        print("\nChoose an option:")
        print("[1] Log Workout")
        print("[2] View Workout History")
        print("[3] Set Fitness Goals")
        print("[4] Help")
        print("[5] Fitness Tips")
        print("[6] Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == "1":
            log_workout()
        elif choice == "2":
            view_workout_history()
        elif choice == "5":
            display_fitness_tips()
        elif choice == "6":
            if confirm_exit():
                sys.exit("\nThank you for using Fitness Tracker CLI! Goodbye!\n")
        else:
            print("\nInvalid option. Please choose a valid option (1-6).\n")

def log_workout():
    """Logs a workout with flexible options, including date, and saves to a file."""
    print("\n" + "=" * 40)
    print("            LOG YOUR WORKOUT          ")
    print("=" * 40)
    
    # Prompt for workout type
    print("\nEnter workout type (e.g., Running, Yoga):")
    print("[1] Running")
    print("[2] Yoga")
    print("[3] Cycling")
    print("[4] Swimming")
    print("[5] Other (type your workout)")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        workout_type = "Running"
    elif choice == "2":
        workout_type = "Yoga"
    elif choice == "3":
        workout_type = "Cycling"
    elif choice == "4":
        workout_type = "Swimming"
    elif choice == "5":
        workout_type = input("Please type the name of your workout: ")
    else:
        print("\nInvalid option. Returning to Home Screen...\n")
        return

    # Prompt for date
    while True:
        date_input = input("Enter the date in YYYY-MM-DD format (e.g., 2024-01-28): ")
        try:
            workout_date = datetime.strptime(date_input, "%Y-%m-%d")
            break  # Exit the loop if the date is valid
        except ValueError:
            print("\nInvalid date format. Please enter the date in YYYY-MM-DD format.")

    # Prompt for workout duration
    duration = input("Enter workout duration (minutes): ")
    notes = input("Optional notes: ")

    # Create the workout entry string
    workout_entry = f"{workout_date.strftime('%Y-%m-%d')} - {workout_type} - {duration} minutes"
    if notes:
        workout_entry += f" - Notes: {notes}"

    # Save to file
    save_workout_to_file(workout_entry)

    print(f"\nYou logged: {workout_entry}\n")

def save_workout_to_file(workout_entry):
    """Saves the workout entry to a text file."""
    try:
        with open("workout_history.txt", "a") as file:
            file.write(workout_entry + "\n")
        print("\nWorkout saved to workout_history.txt.")
    except Exception as e:
        print(f"Error saving workout to file: {e}")

def view_workout_history():
    """Reads and displays the workout history from the file."""
    print("\n" + "=" * 40)
    print("            WORKOUT HISTORY          ")
    print("=" * 40)
    
    if not os.path.exists("workout_history.txt"):
        print("No workout history found.\n")
        return
    
    try:
        with open("workout_history.txt", "r") as file:
            workout_history = file.readlines()
        
        if workout_history:
            for idx, entry in enumerate(workout_history, 1):
                print(f"{idx}. {entry.strip()}")
        else:
            print("No workouts logged yet.\n")
    except Exception as e:
        print(f"Error reading workout history: {e}")

def display_fitness_tips():
    """Displays the basic fitness tips page and handles user selection."""
    while True:
        print("\n" + "=" * 40)
        print("            FITNESS TIPS              ")
        print("=" * 40)
        print("\nTip #1: Consistency is key. Try to log your workouts daily!")
        print("Tip #2: Mix cardio and strength training for a balanced routine.")
        print("Tip #3: Stretching improves flexibility and prevents injury.")

        print("\n[1] More Tips")
        print("[2] Return to Home Screen")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_additional_tips()
        elif choice == "2":
            return  # Redirects back to Home Screen
        else:
            print("\nInvalid option. Please choose 1 or 2.\n")

def display_additional_tips():
    """Displays additional categorized fitness tips."""
    print("\n" + "=" * 40)
    print("           ADDITIONAL TIPS            ")
    print("=" * 40)
    print("\n**Cardio Tips**")
    print("- Start with a warm-up to gradually increase your heart rate.")
    print("- Incorporate intervals to boost calorie burn and endurance.")

    print("\n**Strength Training Tips**")
    print("- Focus on form, not weight, to avoid injuries.")
    print("- Rest between sets to maximize performance.")

    print("\n**General Wellness Tips**")
    print("- Drink water throughout the day, not just during workouts.")
    print("- Aim for at least 7-8 hours of sleep to allow recovery.")

    print("\n[1] Back to Fitness Tips")
    print("[2] Return to Home Screen")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        display_fitness_tips()
    elif choice == "2":
        display_home_screen()  # Now correctly redirects back to Home Screen
    else:
        print("\nInvalid option. Returning to Home Screen...\n")
        display_home_screen()  # Ensures users are sent back to the home screen

def confirm_exit():
    """Displays the exit confirmation screen and returns True if the user confirms exit."""
    print("\n" + "=" * 40)
    print("            EXIT PROGRAM              ")
    print("=" * 40)
    print("\nAre you sure you want to exit?")
    print("[1] Yes")
    print("[2] No")
    print("\n-------------------------------------")
    print("Caution: Exiting now could result in losing unsaved progress or requiring a program restart.")

    exit_choice = input("\nEnter your choice: ")
    
    if exit_choice == "1":
        return True
    elif exit_choice == "2":
        print("\n[Redirecting to Home Screen...]\n")
        return False
    else:
        print("\nInvalid option. Returning to Home Screen...\n")
        return False

# Run the program
display_home_screen()
