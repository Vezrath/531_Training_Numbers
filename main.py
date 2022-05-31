# Calculates the weights to use during training session from current Training Maximum weight (TM)
# Training Program in use will be Wendler-531

# Need to round the numbers to the closest 2,5kg number since most weight rooms don't have smaller than 1,25kg plates
def my_round(x, base=2.5):
    return base * round(x/base)


answer = input("Do you want to use Repetition Maximum or Training Maximum to calculate the weights? (RM/TM)")

if answer == "RM":
    rm = int(input("What is your current Repetition Maximum? "))
    tm = round(0.9 * rm, 2)
elif answer == "TM":
    tm = float(input("What is your current Training Maximum? "))
else:
    print("That is not the correct form of answer for this program.")
    tm = 0

# The Wendler-531 program structure
if tm != 0:
    print(f"Week 1:\nSet 1: {my_round(0.65*tm)}\nSet 2: {my_round(0.75*tm)}\nSet 3: {my_round(0.85*tm)}")
    print(f"Week 2:\nSet 1: {my_round(0.7*tm)}\nSet 2: {my_round(0.8*tm)}\nSet 3: {my_round(0.9*tm)}")
    print(f"Week 3:\nSet 1: {my_round(0.75*tm)}\nSet 2: {my_round(0.85*tm)}\nSet 3: {my_round(0.95*tm)}")
    print(f"Week 4:\nSet 1: {my_round(0.4*tm)}\nSet 2: {my_round(0.5*tm)}\nSet 3: {my_round(0.6*tm)}")

# TODO 4 Save progress in a text file

# TODO 5 Print progress log over time in a xy-function somehow

# TODO 6 Make a GUI for the program
