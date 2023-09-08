# @author   Lucas Cardoso de Medeiros
# @since    19/12/2022
# @version  1.0

# Interactive Coding Exercise


# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        args_text = ""
        for i in range(len(args)):
            args_text = args_text + str(args[i]) + ", "
        args_text = args_text[:-2]
        print(f"You called {function.__name__}({args_text})")

    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a + b + c


if __name__ == "__main__":
    a_function(1, 2, 3)
