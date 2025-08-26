# Part 1 BMI Calculator
def BMI_Calc():
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    BMI = (weight * 703) / (height**2)
    print(f"Your BMI is {BMI:.2f}")
# BMI_Calc()


# Part 2 loop sum of even numbers 2 to 100
def loop_2_100():
    num =0
    for i in range(2,101,2):
        num += i
    print(num)
# loop_2_100()


# Part 3 loop to cimpute the sum of odd number between a and b(user input)
def input_loop():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    num = 0
    for i in range(a,b+1):
        if i%2 == 1:
            num += i
    print(num)
# input_loop()


# Part 4
def sell_stocks():
    goal = float(input("Enter the target price of your stock: "))
    current = float(input("Enter the current price of your stock: "))
    while True:
        if current < goal:
            print("Do not sell your stock")
            current = float(input("What is the new current price of your stock: "))
        else:
            print("Sell your stock!!!")
            break
# sell_stocks()


# Part 5
def tuition_increase():
    num = 8000
    print("Current tuition is $8,000")
    for i in range(1,6):
        num = num * 1.03
        print(f"{i} year(s) later the tuition will be {num:.2f}")
# tuition_increase()
