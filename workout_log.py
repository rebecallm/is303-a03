'''
Rebeca Llontop 
IS 303 - A03

Workout Log
Logs workout sessions and produces fitness statistics

Inputs:
- Name (string)
- Number of workouts (int)
- For each workout: exercise type (string), duration (float), calories burned (float)

Processes:
- Calculate total calories burned by using the accumalting pattern 
- Calculate average duration by diving 
- Max: Find most calories burned in a single workout

Outputs:
- Print name and each workout details
- Print total calories burned, average duration, longest workout.
'''
#Inputs
#name = input("What is your name? ").capitalize()
num_workouts = int(input("How many workouts did you do this week? "))
workouts = {}
#Create the loop for the exercise type, duration, and calories burned
for i in range(num_workouts):
    exercise = input("Enter exercise type: ").capitalize()
    duration = float(input("Enter duration in minutes: "))
    calories = float(input("Enter calories burned: "))
    workouts[exercise] = (duration, calories)
print("your workouts are: ")
for exercise, details in workouts.items():
    print(f"{exercise}: Duration {details[0]} minutes, Calories burned {details[1]} calories")  
#Calculate total calories burned
total_calories = 0
for details in workouts.values():
    total_calories += details[1]
print(f"The total calories burned this week are: {total_calories} calories.")
#Calculate average duration
total_duration = 0
for details in workouts.values():
    total_duration += details[0]
average_duration = total_duration / len(workouts)
print(f"The average duration of your workouts is: {average_duration:.2f} minutes.")
#Find most calories burned in a single workout
max_calories = 0
max_exercise = ""
for exercise, details in workouts.items():
    if details[1] > max_calories:
        max_calories = details[1]
        max_exercise = exercise
print(f"The workout with the most calories burned is {max_exercise} with {max_calories} calories burned.")