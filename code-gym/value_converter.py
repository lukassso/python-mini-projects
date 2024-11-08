def convert_temperature():
    """Prompts user to choose between Celsius to Fahrenheit or Fahrenheit to Celsius conversion.
    Displays the converted temperature."""
    
    print("\nWhich conversion do you want to choose:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            temp = float(input("Enter temperature in Celsius: "))
            print(f"{temp}°C is equal to {(temp * 9/5) + 32}°F.\n")
        elif choice == 2:
            temp = float(input("Enter temperature in Fahrenheit: "))
            print(f"{temp}°F is equal to {(temp - 32) * 5/9}°C.\n")
        else:
            print("Invalid input...please try again.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def convert_currency():
    """Prompts user to choose between USD to GBP or GBP to USD conversion.
    Displays the converted currency based on today's exchange rate."""
    
    EXCHANGE_RATE = 0.82  # Aktualny kurs wymiany
    print("\nWhich conversion do you want to choose:")
    print("1. Dollar to Pound")
    print("2. Pound to Dollar")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            value = float(input("Enter amount in dollars: "))
            print(f"{value} USD is equal to {value * EXCHANGE_RATE} GBP.\n")
        elif choice == 2:
            value = float(input("Enter amount in pounds: "))
            print(f"{value} GBP is equal to {value / EXCHANGE_RATE} USD.\n")
        else:
            print("Invalid input...please try again.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def convert_lengths():
    """Prompts user to choose between centimeters to feet/inches or feet/inches to centimeters.
    Displays the converted length."""
    
    print("\nWhich conversion do you want to choose:")
    print("1. Centimeters to feet and inches")
    print("2. Feet and inches to centimeters")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            value = float(input("Enter length in cm: "))
            inches = value / 2.54
            feet = int(inches // 12)
            remaining_inches = inches % 12
            print(f"{value} cm is equal to {feet} feet and {remaining_inches:.2f} inches.\n")
        elif choice == 2:
            feet = int(input("Enter length in feet: "))
            inches = float(input("Enter length in inches: "))
            length_cm = (feet * 12 + inches) * 2.54
            print(f"{feet} feet and {inches} inches is equal to {length_cm} cm.\n")
        else:
            print("Invalid input...please try again.\n")
    except ValueError:
        print("Please enter valid numeric values.\n")


print("===== Welcome to Value Converter =====")
while True:
    print("\nWhich option would you like to choose:")
    print("1. Convert temperature")
    print("2. Convert currency")
    print("3. Convert lengths")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            convert_temperature()
        elif choice == 2:
            convert_currency()
        elif choice == 3:
            convert_lengths()
        elif choice == 4:
            print('Exiting... Goodbye!')
            break
        else:
            print("Invalid choice, please select a valid option.\n")
    except ValueError:
        print("Please enter a valid numeric option.\n")
