def get_three_integers():
    while True:
        try:
            num1 = int(input("Enter the first integer: "))
            num2 = int(input("Enter the second integer: "))
            num3 = int(input("Enter the third integer: "))
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")

    # Using nested if statements to find the largest number
    if num1 > num2:
        if num1 > num3:
            largest = num1
        else:
            largest = num3
    else:
        if num2 > num3:
            largest = num2
        else:
            largest = num3

    print(f"The largest number is: {largest}")

# Call the function
get_three_integers()