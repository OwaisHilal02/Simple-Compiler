def valid_Var(input_string):
    index = 0
    
    # Function to get the next symbol
    def get_next():
        nonlocal index
        if index < len(input_string):
            symbol = input_string[index]
            index += 1
            return symbol
        else:
            return None
    
    symbol = get_next()
    
    # Check if the variable name starts with "<"
    if symbol == "<":
        symbol = get_next()
        
        # Iterate through each subsequent symbol
        while symbol and (symbol.isalpha() or symbol.isdigit()):
            symbol = get_next()
        
        # Check if the variable name ends with ">;"
        if symbol == ">":
            symbol = get_next()
            if symbol == ";":
                # Check if we have reached the end of the input string
                if not get_next():
                    return True
    return False

def main():
    variables = {}  # Dictionary to store variables and their values

    while True:
        command = input(">>> ")  # Prompt the user to enter a command

        if command.lower() == "exit":
            break  # Exit the loop if the user enters "exit"

        if "=" in command:
            var_name, var_value = command.split("=")
            var_name = var_name.strip()
            var_value = var_value.strip()
            if valid_Var(var_name):
                try:
                    variables[var_name] = eval(var_value, variables)  # Evaluate the variable value expression
                except Exception as e:
                    print("Error:", e)  # Print an error message if an exception occurs
            else:
                print("Invalid variable name. Variable name should start and end with '<' and '>', respectively, and contain only letters and digits in between.")
        elif "+" in command:
            nums = command.split("+")
            nums = [num.strip() for num in nums]
            try:
                num1 = variables[nums[0]]
                num2 = variables[nums[1]]
                print("Sum:", num1 + num2)
            except (ValueError, KeyError, IndexError):
                print("Invalid input or variable names.")
        else:
            try:
                # Check if the command is a variable name
                if command.strip() in variables:
                    print("Value of {}= {}".format(command.strip(), variables[command.strip()]))
                else:
                    print("Error: Variable '{}' is not declared.".format(command.strip()))
            except Exception as e:
                print("Error:", e)  # Print an error message if an exception occurs

if __name__ == "__main__":
    main()
