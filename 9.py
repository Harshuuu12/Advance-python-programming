# Write python program that user to enter only odd numbers, else will
# raise an exception

class evennumber(Exception):
    pass

def get_odd_number():
    while True:
        try:
            user_input = int(input("Enter an odd number: "))
            if user_input % 2 == 0:
                raise evennumber("Even number entered. Please enter an odd number.")
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Example usage
try:
    odd_number = get_odd_number()
    print("You entered an odd number:", odd_number)
except evennumber as e:
    print("Error:", str(e))
