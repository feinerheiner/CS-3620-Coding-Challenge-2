# Part 1
# A. Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:
#       BMI = (weight in Kg)/(Height in Meters)^2.
# B.Write code that can accept the weight and height of a person and calculate their BMI.
#       Make sure to use a function that accepts the height and weight values and returns the BMI value.
def bmi_calculator(weight, height):
    print("This is a BMI calculator.")
    bmi = weight / (height ** 2)
    formant_bmi = "{:.2f}".format(bmi)
    print("The BMI for someone that weighs " + str(weight) + " Kg and is " + str(height) + " meters tall is: "
          + str(formant_bmi))


# Part 2
#   Write a function which would divide two numbers, design the function in
#   a manner that it handles the divide by zero exception.

def divider(a, b):
    try:
        print(a / b)
    except:
        print("A division error has occurred")


# Part 3
#   1. Write Python code to open a file named demo.txt and write some random data into it.
#   2. Open the file, read the contents, and display them as output.
#   3. Write code to add additional text to the existing file on a new line without
#   deleting the previous contents.

def file_write(file):
    f = open(file, "w")
    f.write("This is a new file.")
    f.close()


def file_read(file):
    f = open(file, "r")
    print(f.read())
    f.close()


def file_append(file):
    f = open(file, "a")
    f.write("This is adding to the file.")
    f.close()


# Part 4
#   1. Write code that accepts the name of a product and in turn returns their respective
#   prices.
#       a. Make sure to use a dictionary to store products and their respective prices.
#       b. The dictionary should include at least 5 elements.
games = {
    "Halo": 32.00,
    "Zelda": 62.00,
    "Mario Cart": 40.99,
    "Mario Party": 35.50,
    "Assassins Creed": 50.21
}


def game_inventory(game):
    try:
        print("The price of " + game + " is $" + str(games[game]))
        return games[game]
    except:
        print("Game not found")


# Part 5
#   1. List out all the odd numbers from 1 to 100 using lists in Python.
#       a.use list(), range(), and a for loop with a conditional statement that outputs
#       the numbers.


def odd_numbers():
    number_list = []
    for i in range(1, 101):
        number_list.append(i)
    print(number_list[::2])


# Testing the functions

print("\nTest BMI\n")
bmi_calculator(113, 1.82)

print("\nTest divider\n")
divider(100, 10)
divider(0, 10)
divider(10, 0)

print("\nTest File handler\n")
file_write("demofile.txt")
file_read("demofile.txt")
file_append("demofile.txt")
file_read("demofile.txt")

print("\nTest Dictionary items\n")
game_inventory("Halo")
game_inventory("halo 2")
game_inventory("Assassins Creed")


print("\nTest List splicing\n")
odd_numbers()