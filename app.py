import csv
import random
import time
import sys


# Load drinks from the CSV file
def load_drinks(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader]

# Pick a random drink
def choose_drink(drinks):
    return random.choice(drinks)

# Display a loading animation
def loading_animation():
    print("焼酎を選びます！", end='', flush=True)
    print() 
    for _ in range(3):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print()  # Move to the next line

# Main program
def main():
    drinks = load_drinks('shochu.csv')
    loading_animation()
    drink = choose_drink(drinks)
    print(f"今日は{drink}を飲みましょう！")

if __name__ == '__main__':
    main()
