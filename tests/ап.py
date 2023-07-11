def greet():
    print("Hello, world!")

def perform_action(greet):
    print("Performing action...")
    greet()

# # Передача функции greet в функцию perform_action
perform_action(greet)
