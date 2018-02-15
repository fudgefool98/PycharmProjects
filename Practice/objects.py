def display_menu():
    print('*Electricity Bill Calculator*'
          '\n   (1)    residential'
          '\n   (2)     commercial'
          '\n   (3)     industrial')


def error_check(option):
    if option < 1 or option > 3:
        return True
    else:
        return False


def error_check_units(units):
    if units < 0:
        return True
    else:
        return False


def get_rate(units, option):
    if option == 1:
        if 0 < units <= 300:
            return units * 7.5
        elif 300 < units <= 750:
            return units * 10
        elif 750 < units <= 1500:
            return units * 13.5
        elif units > 1500:
            return units * 15
    elif option == 2:
        if 0 < units <= 300:
            return units * 10.5
        elif 300 < units <= 750:
            return units * 14
        elif 750 < units <= 1500:
            return units * 17.5
        elif units > 1500:
            return units * 20
    elif option == 3:
        if 0 < units <= 300:
            return units * 36.5
        elif 300 < units <= 750:
            return units * 40
        elif 750 < units <= 1500:
            return units * 45.5
        elif units > 1500:
            return units * 50


def bonus(x):
    z = x
    array = []
    for i in range(x):
        array.append(z)
        z -= 1
    array.reverse()
    string = ''.join(str(e) for e in array)
    print("The numbers are: " + string)
    string = sum(array)
    print("the sum of the  numbers from 0 to " + str(x) + " are " + str(string))
    even = 0
    odd = 0
    for x in range(len(array)):
        if x % 2 == 0:
            even += x
        else:
            odd += x
    print("Sum of Even numbers = " + str(even))
    print("Sum of Odd numbers = " + str(odd))


def main():
    print("***** ELECTRICITY BILL CALCULATOR *****")
    display_menu()
    option = int(input("Choose the type of connection: "))
    while error_check(option):
        option = int(input("Invalid Choice! Please enter a valid choice"))
    units = int(input("Enter the number of units(in kWh): "))
    while error_check_units(units):
        units = int(input("Invalid input! Please enter a positive value"))
    result = get_rate(units, option)
    print(result)
    print("Would you like to continue to the bonus?")
    option = int(input("Enter 1 for yes and 0 for no: "))
    if option == 1:
        print("EXITING ELECTRICITY BILL CALCULATOR")
        print("*** BONUS ***")
        positive_number = int(input("Enter a number: "))
        while error_check_units(positive_number):
            positive_number = int(input("Enter a POSITIVE number: "))

        bonus(positive_number)
    else:
        return 0


main()
