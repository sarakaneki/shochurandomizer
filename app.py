import csv
import random

# Load drinks from the CSV file
def load_drinks(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader]

# Pick a random drink
def choose_drink(drinks):
    return random.choice(drinks)

# Main program
def main():
    drinks = load_drinks('drinks.csv')
    drink = choose_drink(drinks)
    print(f"今日は{drink}を飲みましょう！")

if __name__ == '__main__':
    main()
